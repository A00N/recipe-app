from app import app
from flask import redirect, render_template, request, session, abort
from werkzeug.security import check_password_hash, generate_password_hash
from db import db
import secrets


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/control")
def control():
    return render_template("control.html")


@app.route("/add-data", methods=["POST", "GET"])
def addData():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    category = request.form["category"]
    time = request.form["time"]
    price = request.form["price"]
    sql1 = "INSERT INTO categories (category) VALUES (:category)"
    sql2 = "INSERT INTO times (time) VALUES (:time)"
    sql3 = "INSERT INTO prices (price) VALUES (:price)"
    if len(category) > 0:
        db.session.execute(sql1, {"category": category})
    if len(time) > 0:
        db.session.execute(sql2, {"time": time})
    if len(price) > 0:
        db.session.execute(sql3, {"price": price})
    db.session.commit()
    return render_template("control.html")


@app.route("/recipes")
def recipes():
    result = db.session.execute("SELECT id, name, category, time, price FROM recipes")
    recipes = result.fetchall()
    return render_template("recipes.html", count=len(recipes), recipes=recipes)


@app.route("/search", methods=["POST"])
def search():
    value = request.form["order"]
    if value == "1":
        result = db.session.execute("SELECT id, name, category, time, price FROM recipes ORDER BY name ASC")
    elif value == "2":
        result = db.session.execute("SELECT id, name, category, time, price FROM recipes ORDER BY name DESC")
    elif value == "3":
        result = db.session.execute("SELECT id, name, category, time, price FROM recipes ORDER BY LENGTH(price)")
    elif value == "4":
        result = db.session.execute("SELECT id, name, category, time, price FROM recipes ORDER BY LENGTH(price) DESC")
    recipes = result.fetchall()
    return render_template("recipes.html", count=len(recipes), recipes=recipes)


@app.route("/new-recipe")
def newrecipe():
    categoryResult = db.session.execute("SELECT id , category FROM categories")
    timesResult = db.session.execute("SELECT id , time FROM times")
    pricesResult = db.session.execute("SELECT id , price FROM prices")
    categories = categoryResult.fetchall()
    times = timesResult.fetchall()
    prices = pricesResult.fetchall()
    return render_template("new-recipe.html", categories=categories, times=times, prices=prices)


@app.route("/add-recipe", methods=["POST"])
def addrecipe():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    name_taken = False
    name = request.form["name"]
    category = request.form["category"]
    recipe = request.form["recipe"]
    time = request.form["time"]
    price = request.form["price"]
    creator = session["username"]

    name_check = "SELECT name FROM recipes"
    name_result = db.session.execute(name_check)
    recipe_name = name_result.fetchall()

    for names in recipe_name:
        if names[0] == name:
            name_taken = True
    if name_taken:
        categoryResult = db.session.execute("SELECT id , category FROM categories")
        timesResult = db.session.execute("SELECT id , time FROM times")
        pricesResult = db.session.execute("SELECT id , price FROM prices")
        categories = categoryResult.fetchall()
        times = timesResult.fetchall()
        prices = pricesResult.fetchall()
        return render_template("new-recipe.html", name_taken=name_taken, categories=categories, times=times, prices=prices, name=name, recipe=recipe)

    sql = "INSERT INTO recipes (name, category, recipe, time, price) VALUES (:name, :category, :recipe, :time, :price)"
    sql2 = "INSERT INTO data (recipename, creator) VALUES (:recipename, :creator)"
    db.session.execute(sql, {"name": name, "category": category, "recipe": recipe, "time": time, "price": price})
    db.session.execute(sql2, {"recipename": name, "creator": creator})
    db.session.commit()
    return redirect("/recipes")


@app.route("/recipes/<int:id>")
def recipe(id):
    sql = "SELECT id, name, category, recipe, time, price FROM recipes WHERE id=:id"
    result = db.session.execute(sql, {"id": id})
    recipe = result.fetchone()

    find_creator = "SELECT creator FROM data, recipes WHERE data.recipename=recipes.name AND recipes.id=:id"
    creator_result = db.session.execute(find_creator, {"id": id})
    creator_found = creator_result.fetchone()
    try:
        creator = creator_found[0]
    except:
        creator = "Ei luojaa"
    return render_template("recipe.html", id=id, recipe=recipe, creator=creator)


@app.route("/result")
def result():
    prequery = request.args["query"]
    query = prequery.lower()
    sql = "SELECT id, name, category, time, price FROM recipes WHERE lower(name) LIKE :query or lower(category) LIKE :query or time LIKE :query or price LIKE :query"
    result = db.session.execute(sql, {"query": "%" + query + "%"})
    recipes = result.fetchall()
    return render_template("recipes.html", recipes=recipes)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/loginTRUE", methods=["POST"])
def loginTRUE():
    wrong_input=False
    username = request.form["username"]
    password = request.form["password"]
    # Check for user
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        wrong_input = True
        return render_template("login.html", wrong_input=wrong_input)
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            wrong_input = True
            return render_template("login.html",wrong_input=wrong_input)


@app.route("/register", methods=["POST", "GET"])
def register():
    return render_template("register.html")


@app.route("/registerTRUE", methods=["POST", "GET"])
def registerTRUE():
    name_taken = False
    wrong_length = False
    nonmatch = False
    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]
    sql = "SELECT username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if user:
        name_taken = True
    if name_taken:
        return render_template("register.html",name_taken=name_taken)

    if len(username) >= 4 and len(password) >= 5 or len(username) > 15 and len(password) > 15:
        if password == password2:
            hash_value = generate_password_hash(password)
            sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
            db.session.execute(sql, {"username": username, "password": hash_value})
            db.session.commit()
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            nonmatch = True
            return render_template("register.html", nonmatch=nonmatch)
    wrong_length = True
    return render_template("register.html", wrong_length=wrong_length)


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


