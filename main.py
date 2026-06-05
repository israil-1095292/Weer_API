from flask import Flask, render_template, redirect

from weather_api import WeatherAPI
from database import Database
from config import CITY


app = Flask(__name__)

weather_api = WeatherAPI()
database = Database()


@app.route("/")
def dashboard():

    data = weather_api.get_weather(CITY)

    if data is None:
        return "Geen weerdata beschikbaar."

    city = data["name"]
    temp = round(data["main"]["temp"])
    desc = data["weather"][0]["description"]


    history = database.get_history()

    return render_template(
        "index.html",
        city=city,
        temp=temp,
        desc=desc,
        history=history
    )

@app.route("/save", methods=["POST"])
def save_weather():

    data = weather_api.get_weather(CITY)

    city = data["name"]
    temp = round(data["main"]["temp"])
    desc = data["weather"][0]["description"]

    database.insert_weather(
        city,
        temp,
        desc
    )

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)