from app import app
from flask import render_template

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/register")
def register():
	return render_template("regis.html")

@app.route("/login")
def login():
	return render_template("login.html")