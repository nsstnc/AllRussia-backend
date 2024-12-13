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


@jwt.expired_token_loader
@jwt.invalid_token_loader
@jwt.needs_fresh_token_loader
@jwt.unauthorized_loader
def expired_token(*args):
    resp = redirect(url_for("admin_login"))
    unset_jwt_cookies(resp)
    return resp


@app.route('/api/upload_image', methods=['POST'])
@jwt_required()
def upload_image():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'}), 400

    if file and verifyExt(file.filename):
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        try:
            file_path = pathlib.Path(UPLOAD_FOLDER, unique_filename)
            file.save(file_path)
        except Exception as e:
            return jsonify({'success': False, 'error': f'Failed to save file: {str(e)}'}), 500

        file_url = url_for('send_public_file', filename=unique_filename, _external=True)
        return jsonify({'location': file_url}), 200
    else:
        return jsonify({'success': False, 'error': 'Invalid file format'}), 400


@app.route('/api/public/<filename>')
@jwt_required(optional=True)
def send_public_file(filename):
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
        return redirect(url_for('admin_panel'))

    if request.method == 'GET':
        print(error)
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
                print(f"Allow access due to an error: code={resp.status_code}; message={server_output}",
                      file=sys.stderr)
                return True
            return json.loads(server_output)["status"] == "ok"
        except requests.exceptions.Timeout:
            print("Timeout occured")
            return True

    token = request.form["smart-token"]

    if check_captcha(token):
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = database.get_user_by_username(username)

        if user and user['password'] == hashed_password:
            response = redirect(url_for('admin_panel'))
            create_jwt_token(response, user)
            return response
        else:
            error = 'Неправильное имя пользователя или пароль'
            return redirect(url_for("admin_login", error=error))
    else:
        print("Robot")


def create_jwt_token(resp, user):
    token = create_access_token(identity=user['username'], fresh=True)
    set_access_cookies(resp, token)


@app.route('/api/admin_panel/', defaults={'table': 'news', 'page': 1, 'sort': 'updated', 'order': 'desc'})
@app.route('/api/admin_panel/<string:table>', methods=['GET', 'POST'])
@app.route('/api/admin_panel/<string:table>/<int:page>', methods=['GET', 'POST'])
@app.route('/api/admin_panel/<string:table>/<int:page>/<string:sort>/<string:order>', methods=['GET', 'POST'])
@jwt_required()
def admin_panel(table, page=1, sort='updated', order='desc'):
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
    resp = redirect(url_for("admin_login"))
    unset_jwt_cookies(resp)
    return resp


@app.route('/api/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_record(id):
    table = request.args.get('table')
    if table:
        # Удаляем запись из указанной таблицы
        database.delete_record(table, id)
        return jsonify({"success": True, "message": "Запись удалена"}), 200
    else:
        return jsonify({"success": False, "message": "Не указана таблица"}), 400


@app.route('/api/admin_panel/edit/<int:id>/<string:table>', methods=['GET', 'POST'])
@jwt_required()
def edit(id, table):
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
                        print("Не удалось найти файл")
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
        return redirect(url_for('admin_panel', table=table))
    else:
        record = database.get_record_by_id(table, id)
        return render_template('edit_record.html', tables=table_names, table=table, id=id, record=dict(record))


@app.route('/api/admin_panel/add/<string:table>', methods=['GET', 'POST'])
@jwt_required()
def add_record(table):
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

        return redirect(url_for('admin_panel', table=table))
    else:
        columns = database.get_model_columns(table)
        return render_template('add_record.html', tables=table_names, table=table, columns=columns)


@app.route('/api/admin_panel/make_main/<int:id>', methods=['GET'])
@jwt_required()
def make_main(id):
    if request.method == 'GET':
        database.make_main(id)
        return redirect(url_for('admin_panel', table="news"))


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
