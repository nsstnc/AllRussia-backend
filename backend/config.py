import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DB:
    config = {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": int(os.getenv("DB_PORT", 5432)),
        "database": os.getenv("DB_NAME", "allrussia"),
        "username": os.getenv("DB_USERNAME", "postgres"),
        "password": os.getenv("DB_PASSWORD", "postgres")
    }
    driver = "psycopg2"
    dialect = "postgresql"

    @staticmethod
    def get_path():
        return f"{DB.dialect}+{DB.driver}://{DB.config['username']}:{DB.config['password']}@{DB.config['host']}:{DB.config['port']}/{DB.config['database']}"

    @staticmethod
    def get_path_migration():
        return f"{DB.dialect}://{DB.config['username']}:{DB.config['password']}@{DB.config['host']}/{DB.config['database']}"

    @staticmethod
    def create_database():
        try:
            with psycopg2.connect(
                user=DB.config['username'],
                password=DB.config['password'],
                host=DB.config['host'],
                port=DB.config['port'],
                database="postgres"
            ) as connection:
                connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                with connection.cursor() as cursor:
                    cursor.execute(f"CREATE DATABASE {DB.config['database']};")
            logger.info(f"База данных {DB.config['database']} успешно создана")
        except psycopg2.OperationalError as e:
            logger.error(f"Ошибка подключения: {e}")
        except Exception as error:
            logger.error(f"Ошибка при создании базы данных: {error}")
