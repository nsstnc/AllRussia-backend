from flask import Blueprint
from database import database
import json, pathlib
from cosine_similarity import get_nearest_neighbours

get_data_app = Blueprint('get_data_app', __name__)

# database = Database(f"sqlite:///{str(pathlib.Path(__file__).parent.resolve())}/database.db")


@get_data_app.route("/data_all_news")
def data_news_sorted_by_date():
    return json.dumps(database.get_news(sort_by_date_descending=True), ensure_ascii=False)


@get_data_app.route("/data_news_politics")
def data_news_politics():
    return json.dumps(database.get_news(tag='Политика', sort_by_date_descending=True),
                      ensure_ascii=False)


@get_data_app.route("/data_news_economics")
def data_news_economics():
    return json.dumps(database.get_news(tag='Экономика', sort_by_date_descending=True),
                      ensure_ascii=False)


@get_data_app.route("/data_news_science_education")
def data_news_science_education():
    return json.dumps(
        database.get_news(tag='Наука и образование', sort_by_date_descending=True),
        ensure_ascii=False)


@get_data_app.route("/data_news_culture_history")
def data_news_culture_history():
    return json.dumps(database.get_news(tag='Культура и история', sort_by_date_descending=True),
                      ensure_ascii=False)


@get_data_app.route("/data_news_sport")
def sport_data():
    return json.dumps(database.get_news(tag='Спорт', sort_by_date_descending=True),
                      ensure_ascii=False)


@get_data_app.route("/data_news_tourism")
def toursim_data():
    return json.dumps(database.get_news(tag='Туризм', sort_by_date_descending=True),
                      ensure_ascii=False)


@get_data_app.route("/data_news_partners")
def partners_data():
    return json.dumps(database.get_news(tag='Партнёры', sort_by_date_descending=True),
                      ensure_ascii=False)


@get_data_app.route("/data_news_projects")
def projects_data():
    return json.dumps(database.get_news(tag='Проекты', sort_by_date_descending=True),
                      ensure_ascii=False)


@get_data_app.route("/data_main_page")
def main_page():
    main_article = {'main_article': database.get_main_article()}

    ids = get_nearest_neighbours(main_article_id=main_article['main_article'][0]['id'], count_neighbours=6)
    same_as_main = {'same_as_main': database.get_news_by_id(*ids)}

    last_news = {'last_news': json.loads(data_news_sorted_by_date())[:6]}

    politics = {'politics': json.loads(data_news_politics())[:2]}
    economics = {'economics': json.loads(data_news_economics())[:4]}
    science_education = {'science_education': json.loads(data_news_science_education())[:5]}
    culture_history = {'culture_history': json.loads(data_news_culture_history())[:4]}
    sport = {'sport': json.loads(sport_data())[:4]}
    tourism = {'tourism': json.loads(toursim_data())[:4]}
    partners = {'partners': json.loads(partners_data())[:4]}
    projects = {'projects': json.loads(projects_data())[:4]}

    return json.dumps(
        main_article | same_as_main | last_news | politics | economics |
        science_education | culture_history | sport | tourism | partners | projects,
        ensure_ascii=False)


@get_data_app.route("/get_partners")
def get_partners():
    return json.dumps(database.get_partners(), ensure_ascii=False)


@get_data_app.route("/get_contacts")
def get_contacts():
    return json.dumps(database.get_contacts_info(), ensure_ascii=False)
