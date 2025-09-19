from flask import Flask, jsonify
import requests

app = Flask(__name__)
API_KEY = "YOUR_OPENWEATHERMAP_KEY"

@app.route("/weather/<city>")
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
