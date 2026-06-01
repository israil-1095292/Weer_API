import sqlite3


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
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """

        self.conn.execute(query)
        self.conn.commit()

    def insert_weather(self, city, temp, desc):

        query = """
        INSERT INTO weather
        (city, temperature, description)
        VALUES (?, ?, ?)
        """

        self.conn.execute(
            query,
            (city, temp, desc)
        )

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