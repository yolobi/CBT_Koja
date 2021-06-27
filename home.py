from app import app
import jwt
from flask import render_template, request

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/register")
def register():
	return render_template("regis.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/home", methods=['GET'])
def home():
	if request.method == 'GET':
		token = request.cookies.get('auth')
		print(token)
		payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
		auth = payload['sub']
		print(auth)
		return render_template("dashboard.html", user=auth)

@app.route("/profile", methods=['GET'])
def profile():
	if request.method == 'GET':
		token = request.cookies.get('auth')
		payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
		auth = payload['sub']
		return render_template("biodata.html", user=auth)

@app.route("/persyaratan")
def persyaratan():
	return render_template("persyaratan.html")

@app.route("/editbiodata")
def edit_bio():
	return render_template("editbiodata.html")
