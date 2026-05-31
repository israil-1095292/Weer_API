# main.py

from weather_api import WeatherAPI
from database import Database
from models import WeatherRecord
from config import CITY

def main():
    api = WeatherAPI()
    db = Database()

    data = api.get_weather(CITY)

    if data is None:
        return

    city = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    record = WeatherRecord(city, temp, desc)

    print("===== WEATHER DATA =====")
    print(record)

    db.insert_record(record.city, record.temperature, record.description)

    print("\n===== HISTORY =====")
    for row in db.get_all():
        print(row)


if __name__ == "__main__":
    main()