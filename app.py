import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")  # HOMEPAGE
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_recipes")  # RECIPES PAGE
def get_recipes():
    recipes = list(mongo.db.recipes.find())  # gets recipes from database
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])  # SEARCH RECIPES
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find(
        {"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)