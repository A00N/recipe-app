from flask import Flask
from flask import redirect,render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)



@app.route("/")
def index():
	result = db.session.execute("SELECT id, name, category, time, price FROM recipes")
	recipes = result.fetchall()
	return render_template("index.html", recipes=recipes)

@app.route("/recipes")
def recipes():
	result = db.session.execute("SELECT id, name, category, time, price FROM recipes")
	recipes = result.fetchall()
	return render_template("recipes.html", count=len(recipes), recipes=recipes)

@app.route("/new-recipe")
def newrecipe():
	return render_template("new-recipe.html")

@app.route("/add-recipe", methods=["POST"])
def addrecipe():
	name = request.form["name"]
	category = request.form["category"]
	recipe = request.form["recipe"]
	time = request.form["time"]
	price = request.form["price"]
	sql = "INSERT INTO recipes (name, category, recipe, time, price) VALUES (:name, :category, :recipe, :time, :price)"
	db.session.execute(sql, {"name":name,"category":category,"recipe":recipe,"time":time,"price":price})
	db.session.commit()
	return redirect("/recipes")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/loginTRUE",methods=["POST"])
def loginTRUE():
	username = request.form["username"]
	password = request.form["password"]
	#Check for user
	sql = "SELECT id, password FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username": username})
	user = result.fetchone()
	if not user:
		return redirect("/login")
	else:
		hash_value = user.password
		if check_password_hash(hash_value, password):
			session["username"] = username
			return redirect("/")
		else:
			return redirect("/login")

@app.route("/register", methods=["POST", "GET"])
def register():
	return render_template("register.html")

@app.route("/registerTRUE",methods=["POST", "GET"])
def registerTRUE():
	username = request.form["username"]
	password = request.form["password"]

	if len(username)>=4 and len(password)>=5:
		hash_value = generate_password_hash(password)
		sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
		db.session.execute(sql, {"username": username, "password": hash_value})
		db.session.commit()
		return redirect("/login")
	return redirect("/register")

@app.route("/logout")
def logout():
	del session["username"]
	return redirect("/")

@app.route("/result")
def result():
	query = request.args["query"]
	sql = "SELECT name, category, time, price FROM recipes WHERE lower(name) LIKE :query or lower(category) LIKE :query or time LIKE :query or price = :query"
	result = db.session.execute(sql, {"query":"%"+query+"%"})
	recipes = result.fetchall()
	return render_template("recipes.html", recipes=recipes)

@app.route("/recipes/<int:id>")
def recipe(id):
	sql = "SELECT id, name, category, recipe, time, price FROM recipes WHERE id=:id"
	result = db.session.execute(sql, {"id": id})
	recipe = result.fetchone()
	return render_template("recipe.html", id=id, recipe=recipe)