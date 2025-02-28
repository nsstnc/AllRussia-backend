import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify, \
    make_response
from flask_paginate import Pagination, get_page_args
from flask_jwt_extended import *
import pathlib, hashlib, datetime
from get_data import get_data_app
import requests
import sys
import json
import os
import uuid
from flask_cors import CORS
from database import database

app = Flask(__name__, template_folder="templates")

# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Максимальный размер лог-файла до 50 MB
handler = RotatingFileHandler('logs/app.log', maxBytes=50 * 1024 * 1024, backupCount=3)
handler.setLevel(logging.INFO)

# Формат логирования с временной меткой и уровнем логирования
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)

# Добавляем обработчик логов в Flask
app.logger.addHandler(handler)

CORS(app)
app.secret_key = 'all_russia'
app.config['JWT_SECRET_KEY'] = app.secret_key
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(weeks=2)
jwt = JWTManager(app)
app.register_blueprint(get_data_app, url_prefix='/api')
SMARTCAPTCHA_SERVER_KEY = os.getenv('SMARTCAPTCHA_SERVER_KEY')
SMARTCAPTCHA_CLIENT_KEY = os.getenv('SMARTCAPTCHA_CLIENT_KEY')

UPLOAD_FOLDER = str(pathlib.Path(__file__).parent.resolve()) + "/public"

table_names = {
    'partners': 'Partners',
    'contacts': 'Contacts',
    'users': 'Users',
    'news': 'News',
}

# Логгирование запросов
@app.before_request
def log_request_info():
    app.logger.info(f"Request: {request.method} {request.path} - "
                    f"Headers: {dict(request.headers)} - "
                    f"Args: {request.args} - Form: {request.form}")

@app.after_request
def log_response_info(response):
    app.logger.info(f"Response: {response.status_code} - Headers: {dict(response.headers)}")
    return response

@app.teardown_request
def log_teardown(exception=None):
    if exception:
        app.logger.error(f"Error occurred during request processing: {exception}")

@jwt.expired_token_loader
@jwt.invalid_token_loader
@jwt.needs_fresh_token_loader
@jwt.unauthorized_loader
def expired_token(*args):
    app.logger.warning('Token expired or invalid')
    resp = redirect(url_for("admin_login"))
    unset_jwt_cookies(resp)
    return resp

@app.route('/api/upload_image', methods=['POST'])
@jwt_required()
def upload_image():
    app.logger.info("Upload image request received.")
    if 'file' not in request.files:
        app.logger.error("No file part in the request")
        return jsonify({'success': False, 'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        app.logger.error("No selected file")
        return jsonify({'success': False, 'error': 'No selected file'}), 400

    if file and verifyExt(file.filename):
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        try:
            file_path = pathlib.Path(UPLOAD_FOLDER, unique_filename)
            file.save(file_path)
            app.logger.info(f"File saved successfully: {unique_filename}")
        except Exception as e:
            app.logger.error(f"Failed to save file: {str(e)}")
            return jsonify({'success': False, 'error': f'Failed to save file: {str(e)}'}), 500

        file_url = url_for('send_public_file', filename=unique_filename, _external=True)
        return jsonify({'location': file_url}), 200
    else:
        app.logger.error("Invalid file format")
        return jsonify({'success': False, 'error': 'Invalid file format'}), 400

@app.route('/api/public/<filename>')
@jwt_required(optional=True)
def send_public_file(filename):
    app.logger.info(f"Sending public file: {filename}")
    return send_from_directory(UPLOAD_FOLDER, filename)

def verifyExt(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in {'jpg', 'jpeg', 'png'}

@app.route('/api/admin_login', methods=['GET', 'POST'])
@jwt_required(optional=True)
def admin_login():
    error = request.args.get("error")
    jwt_data = get_jwt()
    if jwt_data and jwt_data.get("fresh", False):
        app.logger.info("User already logged in, redirecting to admin panel")
        return redirect(url_for('admin_panel'))

    if request.method == 'GET':
        app.logger.info("Admin login page requested")
        return render_template('admin_login.html', captcha_key=SMARTCAPTCHA_CLIENT_KEY, error=error)

    def check_captcha(token):
        try:
            resp = requests.get(
                "https://smartcaptcha.yandexcloud.net/validate",
                {
                    "secret": SMARTCAPTCHA_SERVER_KEY,
                    "token": token
                },
                timeout=5
            )
            server_output = resp.content.decode()

            if resp.status_code != 200:
                app.logger.error(f"Captcha validation failed: {resp.status_code}; message={server_output}")
                return True
            return json.loads(server_output)["status"] == "ok"
        except requests.exceptions.Timeout:
            app.logger.error("Timeout occurred during captcha validation")
            return True

    token = request.form["smart-token"]

    if check_captcha(token):
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = database.get_user_by_username(username)

        if user and user['password'] == hashed_password:
            app.logger.info(f"User {username} logged in successfully.")
            response = redirect(url_for('admin_panel'))
            create_jwt_token(response, user)
            return response
        else:
            app.logger.warning(f"Failed login attempt for username: {username}")
            error = 'Неправильное имя пользователя или пароль'
            return redirect(url_for("admin_login", error=error))
    else:
        app.logger.warning("Robot detected during login attempt")

def create_jwt_token(resp, user):
    token = create_access_token(identity=user['username'], fresh=True)
    set_access_cookies(resp, token)

@app.route('/api/admin_panel/', defaults={'table': 'news', 'page': 1, 'sort': 'updated', 'order': 'desc'})
@app.route('/api/admin_panel/<string:table>', methods=['GET', 'POST'])
@app.route('/api/admin_panel/<string:table>/<int:page>', methods=['GET', 'POST'])
@app.route('/api/admin_panel/<string:table>/<int:page>/<string:sort>/<string:order>', methods=['GET', 'POST'])
@jwt_required()
def admin_panel(table, sort='', order='desc', page=1):
    app.logger.info(f"Admin panel accessed for table: {table}")
    per_page = 10
    offset = (page - 1) * per_page
    search_query = request.args.get('search_query', '')
    columns = database.get_model_columns(table)

    data, total, main_article = database.get_data_admin_panel(table, search_query, sort, order,
                                                              per_page, offset)
    pagination = Pagination(page=page, per_page=per_page, total=total, record_name='items')

    return render_template('admin_panel.html', tables=table_names, table=table, columns=columns, data=data,
                           main_article=main_article, pagination=pagination, search_query=search_query,
                           sort=sort, order=order, page=page)

@app.route('/api/logout')
def logout():
    app.logger.info("User logged out")
    resp = redirect(url_for("admin_login"))
    unset_jwt_cookies(resp)
    return resp

@app.route('/api/delete/<string:table>/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_record(table, id):
    app.logger.info(f"Deleting record from table {table} with id {id}")
    if table:
        database.delete_record(table, id)
        app.logger.info(f"Record deleted successfully from table {table} with id {id}")
        return jsonify({"success": True, "message": "Запись удалена"}), 200
    else:
        app.logger.error("Table not specified for deletion")
        return jsonify({"success": False, "message": "Не указана таблица"}), 400

@app.route('/api/admin_panel/edit/<int:id>/<string:table>', methods=['GET', 'POST'])
@jwt_required()
def edit(id, table):
    app.logger.info(f"Editing record from table {table} with id {id}")
    if request.method == 'POST':
        data = dict(request.form)
        if 'file' in request.files:
            file = request.files['file']
            if file and verifyExt(file.filename):
                unique_filename = f"{uuid.uuid4()}_{file.filename}"
                file.save(pathlib.Path(UPLOAD_FOLDER, unique_filename))
                if data['url']:
                    try:
                        pathlib.Path(UPLOAD_FOLDER, data['url']).unlink()
                    except FileNotFoundError:
                        app.logger.error("File not found during edit")
                data['url'] = unique_filename

        if table == "news":
            data["updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if 'tag' in data:
                tag_russian, tag_arabian = data["tag"].split("/")
                data["tag"] = tag_russian
                data["tag_arabian"] = tag_arabian
        elif table == "users" and data["password"]:
            data["password"] = hashlib.sha256(data["password"].encode('utf-8')).hexdigest()

        if 'content' in request.form:
            data['content'] = request.form['content']

        database.update_record(table, id, data)
        app.logger.info(f"Record updated successfully in table {table} with id {id}")
        return redirect(url_for('admin_panel', table=table))
    else:
        record = database.get_record_by_id(table, id)
        return render_template('edit_record.html', tables=table_names, table=table, id=id, record=dict(record))

@app.route('/api/admin_panel/add/<string:table>', methods=['GET', 'POST'])
@jwt_required()
def add_record(table):
    app.logger.info(f"Adding new record to table {table}")
    if request.method == 'POST':
        data = dict(request.form)
        if 'file' in request.files:
            file = request.files['file']
            if file and verifyExt(file.filename):
                unique_filename = f"{uuid.uuid4()}_{file.filename}"
                file.save(pathlib.Path(UPLOAD_FOLDER, unique_filename))
                data['url'] = unique_filename

        if 'content' in request.form:
            data['content'] = request.form['content']
        if 'subtitle' in request.form:
            data['subtitle'] = request.form['subtitle']
        if 'subtitle_arabian' in request.form:
            data['subtitle_arabian'] = request.form['subtitle_arabian']

        new_id = database.get_next_id(table)
        data['id'] = new_id
        if table == "users":
            database.create_user(data['username'], data['password'])
        elif table == "news":
            data["updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if 'tag' in data:
                tag_russian, tag_arabian = data["tag"].split("/")
                data["tag"] = tag_russian
                data["tag_arabian"] = tag_arabian
            database.insert_data(table, data)
        else:
            database.insert_data(table, data)

        app.logger.info(f"New record added successfully to table {table}")
        return redirect(url_for('admin_panel', table=table))
    else:
        columns = database.get_model_columns(table)
        return render_template('add_record.html', tables=table_names, table=table, columns=columns)

@app.route('/api/admin_panel/make_main/<int:id>', methods=['GET'])
@jwt_required()
def make_main(id):
    app.logger.info(f"Making news article with id {id} as main")
    if request.method == 'GET':
        database.make_main(id)
        app.logger.info(f"News article with id {id} set as main")
        return redirect(url_for('admin_panel', table="news"))

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
