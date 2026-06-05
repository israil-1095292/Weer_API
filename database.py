import sqlite3
from datetime import datetime
import pytz

class Database:

    def __init__(self):
        self.conn = sqlite3.connect(
            "weather.db",
            check_same_thread=False
        )

        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            description TEXT,
            timestamp DATETIME
        )
        """

        self.conn.execute(query)
        self.conn.commit()

    def insert_weather(self, city, temp, desc):
        timestamp = datetime.now(pytz.timezone("Europe/Amsterdam")).strftime("%Y-%m-%d %H:%M:%S")

        query = """
        INSERT INTO weather
        (city, temperature, description, timestamp)
        VALUES (?, ?, ?, ?)
        """

        self.conn.execute(query, (city, temp, desc, timestamp))
        self.conn.commit()

    def get_history(self):
        query = """
        SELECT city,
               temperature,
               description,
               timestamp
        FROM weather
        ORDER BY id DESC
        LIMIT 10
        """

        return self.conn.execute(query).fetchall()