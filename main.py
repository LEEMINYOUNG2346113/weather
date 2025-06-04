from flask import Flask
import requests

app = Flask(__name__)

@app.route("/weather")
def get_weather():
    city = "Nowon"
    api_key = "f35f3a95a44ea71fe80b85be8cf70f4e"  # OpenWeatherMap API 키
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},KR&appid={api_key}&units=metric"

    try:
        res = requests.get(url, timeout=5)
        if res.status_code != 200:
            return "error"

        data = res.json()
        main = data["weather"][0]["main"].lower()

        if main in ["clear", "clouds", "rain", "snow", "drizzle"]:
            return main
        elif main in ["fog", "haze", "mist", "dust", "smoke"]:
            return "other"
        else:
            return "other"

    except:
        return "error"
