from crypt import methods
from flask import Flask, render_template, redirect, flash, jsonify, session, request


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
        return render_template("search.html")
