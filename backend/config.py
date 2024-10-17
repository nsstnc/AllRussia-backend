import click
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os


class DB():
    host = 'localhost'
    port = 5432
    database = 'allrussia'
    username = 'postgres'
    password = 'postgres'
    driver = "psycopg2"
    dialect = "postgresql"

    @staticmethod
    def get_path():
        return f"{DB.dialect}+{DB.driver}://{DB.username}:{DB.password}@{DB.host}:{DB.port}/{DB.database}"

    @staticmethod
    def create_database():
        try:
            connection = psycopg2.connect(user=DB.username,
                                          password=DB.password,
                                          host=DB.host,
                                          port=DB.port,
                                          database="postgres")

            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cursor = connection.cursor()
            create_db_query = f"CREATE DATABASE {DB.database};"
            cursor.execute(create_db_query)
            cursor.close()
            connection.close()
            print(f"База данных {DB.database} создана")
        except Exception as error:
            print(f"Ошибка при создании базы данных: {error}")
