from databases import SQLiteDatabase
import json, pathlib
database = SQLiteDatabase(f"{str(pathlib.Path(__file__).parent.resolve())}/database.db")
database.connect()
# добавление пользователя админа
database.create_user('admin', 'admin')
