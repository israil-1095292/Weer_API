# weather_api.py

import requests
from config import BASE_URL, API_KEY

class WeatherAPI:
    def get_weather(self, city):
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code != 200:
            print("Fout bij ophalen van API data")
            return None

        return response.json()