from backend.database import database
import json, pathlib

# добавление пользователя админа
database.create_user('admin', 'admin')
