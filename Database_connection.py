import sqlite3

class Database_connection:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def create_table(self, table_name, columns):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS "+table_name+" ("+columns+")")
        self.connection.commit()

    def insert(self, table_name,coloms, values):
        self.cursor.execute("INSERT INTO "+table_name+" ("+coloms+")VALUES ("+values+")")
        self.connection.commit()

    def select(self, table_name, columns, condition):
        self.cursor.execute("SELECT "+columns+" FROM "+table_name+" WHERE "+condition)
        return self.cursor.fetchall()

    def update(self, table_name, columns, condition):
        self.cursor.execute("UPDATE "+table_name+" SET "+columns+" WHERE "+condition)
        self.connection.commit()