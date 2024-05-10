import psycopg2
import os

def db_connect():
    try:
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_NAME = os.getenv("DB_NAME")

        db_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        return db_connection
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database', e)