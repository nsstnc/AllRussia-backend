from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Модель для таблицы contacts
class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(Text, nullable=True)
    correspondence_address = Column(Text, nullable=True)
    email = Column(String, nullable=True)
    phones = Column(Text, nullable=True)


# Модель для таблицы main_article
class MainArticle(Base):
    __tablename__ = "main_article"

    id = Column(Integer, primary_key=True, index=True)


# Модель для таблицы news
class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, nullable=True)
    title = Column(String, nullable=True)
    title_arabian = Column(String, nullable=True)
    subtitle = Column(String, nullable=True)
    subtitle_arabian = Column(String, nullable=True)
    tag = Column(String, nullable=True)
    tag_arabian = Column(String, nullable=True)
    updated = Column(String, nullable=True)


# Модель для таблицы partners
class Partner(Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, nullable=True)
    title = Column(String, nullable=True)


# Модель для таблицы users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=True)
