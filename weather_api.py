import requests
from config import API_KEY, BASE_URL


class WeatherAPI:

    def get_weather(self, city):

        url = (
            f"{BASE_URL}"
            f"?q={city}"
            f"&appid={API_KEY}"
            f"&units=metric"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return None

        return response.json()