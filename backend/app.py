from flask import Flask, request, render_template, redirect, url_for, session
from databases import SQLiteDatabase
import json, pathlib, hashlib

database = SQLiteDatabase(f"{str(pathlib.Path(__file__).parent.resolve())}/database.db")
app = Flask(__name__, template_folder="templates")
app.secret_key = 'all_russia'


@app.route("/data_news")
def data_news():
    return json.dumps(database.get_all_posts_news())


@app.route("/data_contacts")
def data_contacts():
    return json.dumps(database.get_contacts_info())


@app.route("/data_main_page")
def data_main_page():
    return json.dumps(database.get_main_page_news())


@app.route("/data_articles")
def data_articles():
    return json.dumps(database.get_all_posts_articles())


@app.route("/data_partners")
def data_partners():
    return json.dumps(database.get_all_partners())


@app.route('/add', methods=['POST'])
def add():
    data = request.json
    url = data['url']
    title = data['title']
    subtitle = data['subtitle']
    tag = data['tag']
    database.add_post(url, title, subtitle, tag)
    return data


# маршрут страницы формы для входа в админ-панель
@app.route('/adm_login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        # имя пользователя из формы
        username = request.form['username']
        # пароль из формы
        password = request.form['password']
        # шифруем пароль в sha-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # получаем пользователя из БД с таким именем
        user = database.select_one('SELECT * FROM users WHERE username = ?', (username,))

        # проверяем сходятся ли данные формы с данными БД
        if user and user['password'] == hashed_password:
            # в случае успеха создаем сессию в которую записываем id пользователя
            session['user_id'] = user['id']
            # и делаем переадресацию пользователя на новую страницу -> в нашу адимнку
            return redirect(url_for('admin_panel'))

        else:
            error = 'Неправильное имя пользователя или пароль'

    # Если GET запрос, показываем форму входа
    return render_template('admin_login.html', error=error)


# маршрут страницы админ-панели c выбранной таблицей
@app.route('/admin_panel/', defaults={'table': 'news'})
@app.route('/admin_panel/<string:table>', methods=['GET', 'POST'])
def admin_panel(table):
    # названия таблиц
    tables = list(map(lambda x: x[1], database.get_all_tables()))
    # если пользователь не в сессии, то отправляем его на страницу входа
    if 'user_id' not in session:
        return redirect(url_for('admin_login'))
    # названия колонок таблицы в базе данных
    columns = list(map(lambda x: x[0], database.cursor.execute('SELECT * FROM "{}"'.format(table)).description))
    data = database.select_all('SELECT * FROM "{}"'.format(table))

    # Загрузка и отображение админ-панели
    return render_template('admin_panel.html', tables=tables, table=table, columns=columns, data=data)


# маршрут выхода из админ-панели
@app.route('/logout')
def logout():
    # Удаление данных пользователя из сессии
    session.clear()
    # Перенаправление на страницу входа
    return redirect(url_for("admin_login"))


@app.route('/admin_panel/delete/<int:id>/<string:table>', methods=['GET', 'POST'])
def delete(id, table):
    database.execute('DELETE FROM {} WHERE id =?;'.format(table), (id,))
    print("delete", id, table)
    return redirect(url_for('admin_panel', table=table))

@app.route('/admin_panel/edit/<int:id>/<string:table>', methods=['GET', 'POST'])
def edit(id, table):
    if request.method == 'POST':
        data = request.form
        query = f"UPDATE {table} SET "
        for key in data.keys():
            query += f"{key} = ?, "
        query = query[:-2]
        query += " WHERE id = ?;"
        values = list(data.values())
        values.append(id)
        database.execute(query, tuple(values))
        return redirect(url_for('admin_panel', table=table))
    else:
        record = database.select_one(f'SELECT * FROM {table} WHERE id=?', (id,))
        columns = record.keys()
        record_dict = dict(record)
        return render_template('edit_record.html', table=table, id=id, record=record_dict)

@app.route('/admin_panel/add/<string:table>', methods=['GET', 'POST'])
def add_record(table):
    if request.method == 'POST':
        data = request.form
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data.keys()])
        values = list(data.values())

        last_id = database.select_one(f'SELECT MAX(id) FROM {table}')[0]
        new_id = last_id + 1 if last_id is not None else 1  

        columns += ', id'
        placeholders += ', ?'
        values.append(new_id)

        database.execute(f"INSERT INTO {table} ({columns}) VALUES ({placeholders})", tuple(values))

        return redirect(url_for('admin_panel', table=table))
    else:
        columns = [column[1] for column in database.cursor.execute('PRAGMA table_info({})'.format(table)).fetchall()]
        return render_template('add_record.html', table=table, columns=columns)


print(__name__)
if __name__ == "__main__":
    database.connect()

    app.run(port=5000, debug=True)
