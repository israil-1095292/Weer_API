# database.py

import sqlite3

class Database:
    def __init__(self, db_name="weather.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            description TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_record(self, city, temp, desc):
        query = """
        INSERT INTO weather (city, temperature, description)
        VALUES (?, ?, ?)
        """
        self.conn.execute(query, (city, temp, desc))
        self.conn.commit()

    def get_all(self):
        query = "SELECT * FROM weather"
        return self.conn.execute(query).fetchall()