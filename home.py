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

@app.route("/home")
def home():
	return render_template("dashboard.html")

@app.route("/profil")
def home():
	return render_template("biodata.html")

@app.route("/editbiodata")
def home():
	return render_template("editbiodata.html")