from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory, jsonify, send_file, flash
from flask_paginate import Pagination, get_page_args
from database import Database
from flask_jwt_extended import *
import pathlib, hashlib, datetime
from get_data import get_data_app
import random
import string
from captcha.image import ImageCaptcha  # Для локальной капчи
import requests
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
app.register_blueprint(get_data_app)

# Путь к изображениям
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


# Генерация текста капчи
def generate_captcha_text(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


# Маршрут для изображения капчи
@app.route('/captcha_image')
def captcha_image():
    captcha_text = generate_captcha_text()
    session['captcha_text'] = captcha_text  # Сохраняем текст капчи в сессии
    image = ImageCaptcha(width=365, height=90)
    captcha_image_data = image.generate(captcha_text)
    return captcha_image_data.read(), 200, {'Content-Type': 'image/png'}


# Страница для входа в админ-панель
@app.route('/admin_login', methods=['GET', 'POST'])
@jwt_required(optional=True)
def admin_login():
    error = None
    jwt_data = get_jwt()
    if jwt_data and jwt_data.get("fresh", False):
        return redirect(url_for('admin_panel'))

    if request.method == 'POST':
        # Имя пользователя и пароль
        username = request.form['username']
        password = request.form['password']
        captcha_input = request.form['captcha']  # Получаем ввод капчи
        
        # Проверка капчи
        if captcha_input != session.get('captcha_text'):
            flash('Неверно введен текст с изображения', 'danger')
            return redirect(url_for('admin_login'))

        # Проверка пользователя
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = database.get_user_by_username(database.get_session(), username)

        if user and user['password'] == hashed_password:
            response = redirect(url_for('admin_panel'))
            create_jwt_token(response, user)
            return response
        else:
            error = 'Неправильное имя пользователя или пароль'

    return render_template('admin_login.html', error=error)


def create_jwt_token(resp, user):
    token = create_access_token(identity=user['username'], fresh=True)
    set_access_cookies(resp, token)


@app.route('/admin_panel/', defaults={'table': 'news', 'page': 1, 'sort': 'updated', 'order': 'desc'})
@app.route('/admin_panel/<string:table>', methods=['GET', 'POST'])
@app.route('/admin_panel/<string:table>/<int:page>', methods=['GET', 'POST'])
@app.route('/admin_panel/<string:table>/<int:page>/<string:sort>/<string:order>', methods=['GET', 'POST'])
@jwt_required()
def admin_panel(table, page=1, sort='updated', order='desc'):
    per_page = 10
    offset = (page - 1) * per_page

    search_query = request.args.get('search_query', '')
    columns = database.get_model_columns(table)
    data, total, main_article = database.get_data_admin_panel(
        database.get_session(), table, search_query, sort, order, per_page, offset
    )
    pagination = Pagination(page=page, per_page=per_page, total=total, record_name='items')

    return render_template('admin_panel.html', tables=table_names, table=table, columns=columns, data=data,
                           main_article=main_article, pagination=pagination, search_query=search_query,
                           sort=sort, order=order, page=page)


@app.route('/logout')
def logout():
    resp = redirect(url_for("admin_login"))
    unset_jwt_cookies(resp)
    return resp


@app.route('/admin_panel/delete/<int:id>/<string:table>', methods=['GET', 'POST'])
@jwt_required()
def delete(id, table):
    database.delete_record(database.get_session(), table, id)
    return redirect(url_for('admin_panel', table=table))


@app.route('/admin_panel/edit/<int:id>/<string:table>', methods=['GET', 'POST'])
@jwt_required()
def edit(id, table):
    if request.method == 'POST':
        data = dict(request.form)
        if 'file' in request.files:
            file = request.files['file']
            if file and verifyExt(file.filename):
                unique_filename = f"{uuid.uuid4()}_{file.filename}"
                file.save(pathlib.Path(UPLOAD_FOLDER, unique_filename))
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

        if 'content' in request.form:
            data['content'] = request.form['content']

        database.update_record(database.get_session(), table, id, data)
        return redirect(url_for('admin_panel', table=table))
    else:
        record = database.get_record_by_id(database.get_session(), table, id)
        columns = record.keys()
        record_dict = dict(record)
        return render_template('edit_record.html', tables=table_names, table=table, id=id, record=record_dict)


@app.route('/admin_panel/add/<string:table>', methods=['GET', 'POST'])
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

        new_id = database.get_next_id(database.get_session(), table)
        data['id'] = new_id
        if table == "users":
            database.create_user(database.get_session(), data['username'], data['password'])
        else:
            database.insert_data(database.get_session(), table, data)

        return redirect(url_for('admin_panel', table=table))
    else:
        columns = database.get_model_columns(table)
        return render_template('add_record.html', tables=table_names, table=table, columns=columns)


@app.route('/admin_panel/make_main/<int:id>', methods=['GET'])
@jwt_required()
def make_main(id):
    if request.method == 'GET':
        database.make_main(database.get_session(), id)
        return redirect(url_for('admin_panel', table="news"))


@app.route('/uploads/<filename>')
@jwt_required()
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


def verifyExt(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in {'jpg', 'jpeg', 'png'}


@app.route('/upload_image', methods=['POST'])
@jwt_required()
def upload_image():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'})

    if file and verifyExt(file.filename):
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        file.save(pathlib.Path(UPLOAD_FOLDER, unique_filename))
        return jsonify({'success': True, 'location': url_for('send_file', filename=unique_filename)})
    else:
        return jsonify({'success': False, 'error': 'Invalid file format'})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
