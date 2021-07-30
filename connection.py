import pymysql

from config import DATABASE_CONFIG

def connect_db():

    conn = pymysql.connect(
        host=DATABASE_CONFIG['host'],
        user=DATABASE_CONFIG['user'],
        password=DATABASE_CONFIG['password'],
        db=DATABASE_CONFIG['dbname'],
        port=DATABASE_CONFIG['port']
    )

    return conn
