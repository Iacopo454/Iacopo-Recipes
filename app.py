import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env # noqa


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


@app.route("/register", methods=["GET", "POST"])  # REGISTER
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # if username exists
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        # create username/password
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])  # LOGIN
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])  # PROFILE PAGE
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find())
    # if existing user display profile
    if session["user"]:
        return render_template("profile.html",
                               username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")  # LOGOUT
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])  # ADD RECIPE
def add_recipe():
    if request.method == "POST":
        recipe_vegetarian = "on" if request.form.get(
            "recipe_vegetarian") else "off"
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_vegetarian": recipe_vegetarian,
            "recipe_addedby": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added!")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html")


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])  # EDIT RECIPE
def edit_recipe(recipe_id):
    if request.method == "POST":
        recipe_vegetarian = "on" if request.form.get(
            "recipe_vegetarian") else "off"
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_image": request.form.get("recipe_image"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "recipe_serves": request.form.get("recipe_serves"),
            "recipe_time": request.form.get("recipe_time"),
            "recipe_vegetarian": recipe_vegetarian,
            "recipe_addedby": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe updated!")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")  # DELETE RECIPE
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe deleted!")
    return redirect(url_for("get_recipes"))


@app.route("/recipe_details/<recipe_id>")  # RECIPE DETAILS
def recipe_details(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_details.html", recipe=recipe)


@app.errorhandler(404)  # 404 ERROR
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)  # 500 ERROR
def something_wrong(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)