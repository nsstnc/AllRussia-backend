from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from database import database
import json, pathlib

import string


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower()


def get_nearest_neighbours(main_article_id, count_neighbours):
    # database = Database(f"sqlite:///{str(pathlib.Path(__file__).parent.parent.resolve())}/database.db")

    # 100 последних заголовков новостей из базы данных
    rows = database.get_latest_news_titles(main_article_id)
    df1 = pd.DataFrame(rows, columns=['id', 'title'])

    main_article = database.get_main_article()
    df2 = pd.DataFrame(main_article, columns=['id', 'title'])

    df_news = pd.concat([df1, df2], ignore_index=True).drop_duplicates()

    df_news = df_news.sort_index()

    df_news['title'] = df_news['title'].apply(remove_punctuation)

    vectorizer = CountVectorizer()
    word_weight = vectorizer.fit_transform(df_news['title'])
    nn = NearestNeighbors(metric='cosine')
    nn.fit(word_weight)

    main_index = df_news.index[df_news['id'] == main_article_id].tolist()[0]

    distances, indices = nn.kneighbors(word_weight[main_index], n_neighbors=count_neighbours + 1)

    neighbors = pd.DataFrame({'distance': distances.flatten(), 'index': indices.flatten()}).set_index('index')

    # nearest_info = (
    #     df_news.merge(neighbors, right_on='id', left_index=True).sort_values('distance')[['id', 'title', 'distance']])
    # print(nearest_info)

    result = list(df_news.merge(neighbors, left_index=True, right_index=True).sort_values('distance')['id'])[1:]

    # print(df_news)
    # print(neighbors)
    # print(result)
    return result
