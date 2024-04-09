from flask import Blueprint
from databases import SQLiteDatabase
import json, pathlib

get_data_app = Blueprint('get_data_app', __name__)

database = SQLiteDatabase(f"{str(pathlib.Path(__file__).parent.resolve())}/database.db")
database.connect()


@get_data_app.route("/data_all_news")
def data_news_sorted_by_date():
    return json.dumps(database.get_news(sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_politics")
def data_news_politics():
    return json.dumps(database.get_news(tag='Политика', sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_economics")
def data_news_economics():
    return json.dumps(database.get_news(tag='Экономика', sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_science_education")
def data_news_science_education():
    return json.dumps(database.get_news(tag='Наука и образование', sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_culture_history")
def data_news_culture_history():
    return json.dumps(database.get_news(tag='Культура и история', sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_sport")
def sport_data():
    return json.dumps(database.get_news(tag='Спорт', sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_tourism")
def toursim_data():
    return json.dumps(database.get_news(tag='Туризм', sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_partners")
def partners_data():
    return json.dumps(database.get_news(tag='Партнеры', sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_projects")
def projects_data():
    return json.dumps(database.get_news(tag='Проекты', sort_by_date_descending=True), ensure_ascii=False)