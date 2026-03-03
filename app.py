import os
from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    url = "https://api.coincap.io/v2/assets"

    try:
        response = requests.get(url, timeout=10, headers={
                                "User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        data = response.json()
        coins = data.get("data", [])[:20]  # get first 20 coins
    except Exception as e:
        print("API ERROR:", e)
        coins = []

    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        "index.html",
        coins=coins,
        last_updated=last_updated
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
