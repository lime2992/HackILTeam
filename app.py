from crypt import methods
from flask import Flask, render_template, redirect, flash, jsonify, session, request

from utils import get_latest_news, get_trending_tweets

app = Flask(__name__)


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Index page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
    # User reached route via POST (as by submitting a form via POST)
    # submit the form
        news = request.form.get("news")
    else:
        return render_template("layout.html")

@app.route('/news')
def news_headlines():
    news_articles = get_latest_news()
    return render_template("news.html", news_articles=news_articles)

@app.route('/tweets')
def trending_tweets():
    tweets = get_trending_tweets()
    return render_template("tweets.html", tweets=tweets)
