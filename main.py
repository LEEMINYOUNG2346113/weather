from flask import Flask
import requests

app = Flask(__name__)  # ✅ 먼저 선언

@app.route("/")
def index():
    return "Server is running"

@app.route("/weather")
def get_weather():
    city = "Seoul"
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},KR&appid={api_key}&units=metric"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code != 200:
            return "error"
        data = res.json()
        main = data["weather"][0]["main"].lower()
        if main in ["clear", "clouds", "rain", "snow", "drizzle"]:
            return main
        return "other"
    except:
        return "error"
