import sqlite3
import hashlib
from typing import List
from post import Post
from partner import Partner
from contact import Contact

class SQLiteDatabase():
    def __init__(self, full_filename : str):
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

    def execute(self, query : str, args = ''):
        try:
            self.cursor.execute(query, args)
            self.connection.commit()     
        except Exception as e:
            print(e.with_traceback())

    def select_all(self, query : str, args = ''):
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchall()    
        except Exception as e:
            print(e)
            return []
        
    def select_one(self, query : str, args = ''):
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchone()    
        except Exception as e:
            print(e.with_traceback())
            return []
        
    def add_post_news(self, url, title, subtitle, tag, block) -> None:
        self.execute(f"INSERT INTO news (url, title, subtitle, tag, block) VALUES ('{url}', '{title}', '{subtitle}', '{tag}', '{block}')")

    def get_all_posts_news(self) -> List[Post]:
        return [Post(id, url, title, subtitle, tag, block).__dict__ for id, url, title, subtitle, tag, block in
                self.select_all("SELECT * FROM news")]
    
    def add_post_articles(self, url, title, subtitle, tag) -> None:
        self.execute(f"INSERT INTO articles (url, title, subtitle, tag) VALUES ('{url}', '{title}', '{subtitle}', '{tag}')")

    def get_all_posts_articles(self) -> List[Post]:
        return [Post(id, url, title, subtitle, tag).__dict__ for id, url, title, subtitle, tag in
                self.select_all("SELECT * FROM articles")]
                
    def get_all_partners(self) -> List[Post]:
        return [Partner(id, url, title).__dict__ for id, url, title in
                self.select_all("SELECT * FROM partners")]

    def set_two_cards_section_news(self, id1, id2) -> None:
        self.execute(f"UPDATE news SET block='two_cards_section' WHERE id IN ({id1}, {id2})")

    def set_four_cards_section_news(self, id1, id2, id3, id4) -> None:
        self.execute(f"UPDATE news SET block='four_cards_section' WHERE id IN ({id1}, {id2}, {id3}, {id4})")

    def set_bad_news(self, id1, id2, id3) -> None:
        self.execute(f"UPDATE news SET block='bad_news' WHERE id IN ({id1}, {id2}, {id3})")

    def set_last_news(self, id1, id2, id3, id4, id5) -> None:
        self.execute(f"UPDATE news SET block='last_news' WHERE id IN ({id1}, {id2}, {id3}, {id4}, {id5})")

    def get_main_page_news(self):
        main_news = [Post(id, url, title, subtitle, tag, block).__dict__ for id, url, title, subtitle, tag, block in
                       self.select_all("SELECT * FROM news WHERE block='main_news'")]
        two_section_news = [Post(id, url, title, subtitle, tag, block).__dict__ for id, url, title, subtitle, tag, block in
                self.select_all("SELECT * FROM news WHERE block='two_cards_section'")]
        four_section_news = [Post(id, url, title, subtitle, tag, block).__dict__ for id, url, title, subtitle, tag, block in
                       self.select_all("SELECT * FROM news WHERE block='four_cards_section'")]
        bad_news = [Post(id, url, title, subtitle, tag, block).__dict__ for id, url, title, subtitle, tag, block in
                self.select_all("SELECT * FROM news WHERE block='bad_news'")]
        last_news = [Post(id, url, title, subtitle, tag, block).__dict__ for id, url, title, subtitle, tag, block in
                       self.select_all("SELECT * FROM news WHERE block='last_news'")]

        return [{
                "main_news": main_news,
                "two_section_news": two_section_news,
                "four_section_news": four_section_news,
                "bad_news": bad_news,
                "last_news": last_news}]

    def get_contacts_info(self):
        return [Contact(id, address, correspondence_address, email, phones, url).__dict__ for id, address, correspondence_address, email, phones, url in
                self.select_all("SELECT * FROM contacts")]

    def create_user(self, username: str, password: str):
        # Хеширование пароля
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Добавление нового пользователя
        self.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))

    def get_all_tables(self):
        self.cursor.execute("SELECT * FROM sqlite_master WHERE type='table';")
        return self.cursor.fetchall()
