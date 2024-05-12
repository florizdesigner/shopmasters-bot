import psycopg2
import os
import logging

# настройка формата логирования
logging.basicConfig(filename="../logs/employees.log", filemode="w", format="[%(asctime)s] | [%(levelname)s] | %(message)s", level="INFO")

def db_connect():
    try:
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_HOST = os.getenv("DB_HOST")
        DB_NAME = os.getenv("DB_NAME")

        db_connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
        logging.info(msg="Connect to database is successful!")
        return db_connection
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        logging.error(msg=f"Can't establish connection to database: {e}")