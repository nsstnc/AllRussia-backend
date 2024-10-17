class DB():
    host = 'localhost'
    port = 5432
    database = 'allRussia'
    username = 'postgres'
    password = 'postgres'
    driver = "psycopg2"
    dialect = "postgresql"

    @staticmethod
    def get_path():
        return f"{DB.dialect}+{DB.driver}://{DB.username}:{DB.password}@{DB.host}:{DB.port}/{DB.database}"
