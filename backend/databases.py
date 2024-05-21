import json
import sqlite3
import hashlib
from typing import List
from post import Post
from partner import Partner
from contact import Contact


class SQLiteDatabase():
    def __init__(self, full_filename: str):
        self.full_filename = full_filename

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.full_filename, check_same_thread=False)
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
            if (self.connection):
                self.connection.close()
                print("Соединение с SQLite закрыто")

    def execute(self, query: str, args=''):
        try:
            self.cursor.execute(query, args)
            self.connection.commit()
        except Exception as e:
            print(e.with_traceback())

    def select_all(self, query: str, args=''):
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return []

    def select_one(self, query: str, args=''):
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchone()
        except Exception as e:
            print(e.with_traceback())
            return []

    def get_contacts_info(self):
        return [Contact(id, address, correspondence_address, email, phones).__dict__ for
                id, address, correspondence_address, email, phones in
                self.select_all("SELECT * FROM contacts")]

    def create_user(self, username: str, password: str):
        # Хеширование пароля
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Добавление нового пользователя
        self.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

    def get_all_tables(self):
        self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
        return self.cursor.fetchall()

    # def get_news_politics(self):
    #     return [Post(id, url, title, subtitle, tag, block, updated).__dict__ for id, url, title, subtitle, tag, block, updated in
    #             self.select_all("SELECT id, url, title, subtitle, tag, block, updated FROM news WHERE tag='Политика' ORDER BY updated DESC")]
    #
    # def get_news_economics(self):
    #     return [Post(id, url, title, subtitle, tag, block, updated).__dict__ for id, url, title, subtitle, tag, block, updated in
    #             self.select_all("SELECT id, url, title, subtitle, tag, block, updated FROM news WHERE tag='Экономика' ORDER BY updated DESC")]
    #
    # def get_news_science_education(self):
    #     return [Post(id, url, title, subtitle, tag, block, updated).__dict__ for id, url, title, subtitle, tag, block, updated in
    #             self.select_all("SELECT id, url, title, subtitle, tag, block, updated FROM news WHERE tag='Наука и образование' ORDER BY updated DESC")]
    #
    # def get_news_culture_history(self):
    #     return [Post(id, url, title, subtitle, tag, block, updated).__dict__ for id, url, title, subtitle, tag, block, updated in
    #             self.select_all("SELECT id, url, title, subtitle, tag, block, updated FROM news WHERE tag='Культура и история' ORDER BY updated DESC")]
    #
    # def get_news_sorted_by_date(self):
    #     return [Post(id, url, title, subtitle, tag, block, updated).__dict__ for id, url, title, subtitle, tag, block, updated in
    #             self.select_all("SELECT id, url, title, subtitle, tag, block, updated FROM news ORDER BY updated DESC")]

    def get_news(self, tag=None, sort_by_date_descending=False):
        query = "SELECT id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated FROM news"

        if tag:
            query += f" WHERE tag='{tag}'"

        if sort_by_date_descending:
            query += " ORDER BY updated DESC"

        return [Post(id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated).__dict__ for id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated in
                self.select_all(query)]

    def get_main_article(self):
        query = "SELECT id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated FROM news WHERE id IN (SELECT id FROM main_article)"
        return [Post(id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated).__dict__ for id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated in
                self.select_all(query)]

    def get_news_by_id(self, *args):
        placeholders = ', '.join([str(i) for i in args])
        print(placeholders)
        query = f"SELECT id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated FROM news WHERE id IN ({placeholders})"

        return [Post(id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated).__dict__ for id, url, title, title_arabian, subtitle, subtitle_arabian, tag, tag_arabian, updated in
                self.select_all(query)]

    def get_partners(self):
        return [Partner(id, url, title).__dict__ for
                id, url, title in
                self.select_all("SELECT * FROM partners")]