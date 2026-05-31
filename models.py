# models.py

class WeatherRecord:
    def __init__(self, city, temperature, description):
        self.city = city
        self.temperature = temperature
        self.description = description

    def __str__(self):
        return f"{self.city}: {self.temperature}°C, {self.description}"