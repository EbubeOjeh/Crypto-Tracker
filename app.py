import os
from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }

    try:
    response = requests.get(
        url,
        params=params,
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()
    coins = response.json()


except Exception as e:
    print("API ERROR:", e)
    coins = []

    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html",
                           coins=coins,
                           last_updated=last_updated)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
