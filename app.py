from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return  "<b>Tervetuloa</b> <i> sovellukseen</i>!"
