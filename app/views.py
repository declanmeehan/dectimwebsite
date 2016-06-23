from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
	page = "index"
	return render_template("index.html", page = "index")
	