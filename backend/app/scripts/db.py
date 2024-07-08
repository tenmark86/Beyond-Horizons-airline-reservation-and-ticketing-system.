import mysql.connector
from flask import current_app


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=current_app.config['MYSQL_HOST'],
            port=current_app.config['MYSQL_PORT'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            database=current_app.config['MYSQL_DB'])
        return connection
    except Exception as ex:
        print("Could not connect to database\n", ex)
        return None

