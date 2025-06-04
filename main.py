@app.route("/weather")
def get_weather():
    city = "Seoul"  # ✅ 고쳤음
    api_key = "f35f3a95a44ea71fe80b85be8cf70f4e"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},KR&appid={api_key}&units=metric"

    try:
        res = requests.get(url, timeout=5)
        if res.status_code != 200:
            return f"API Error: {res.status_code}, {res.text}"

        data = res.json()
        main = data["weather"][0]["main"].lower()

        if main in ["clear", "clouds", "rain", "snow", "drizzle"]:
            return main
        elif main in ["fog", "haze", "mist", "dust", "smoke"]:
            return "other"
        else:
            return "other"

    except Exception as e:
        return f"error: {str(e)}"
