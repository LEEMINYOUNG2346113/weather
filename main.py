from flask import Flask
import requests
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render가 할당한 포트 사용
    app.run(host="0.0.0.0", port=port)
