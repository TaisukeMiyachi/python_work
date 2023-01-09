import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
import random

app = Flask(__name__)


@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")


@app.route("/api/recommend_article")
def api_recommend_article():
    with urlopen("http://feeds.feedburner.com/hatena/b/hotentry") as res:
        html = res.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("item")
    random.shuffle(items)

    return json.dumps({
        "content": items[0].find("title").string,
        # "link" : item.find("link").string
        "link": items[0].get('rdf:about')
    })


if __name__ == "__main__":
    app.run(debug=True, port=5004)
