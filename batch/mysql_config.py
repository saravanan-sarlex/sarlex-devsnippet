import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="admin",
        database="devsnippet",
        charset="utf8mb4"
    )
    return connection

