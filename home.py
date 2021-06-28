from flask.helpers import make_response
from app import app
import jwt
from flask import render_template, request, redirect, url_for

check = 0

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
	if (request.method == 'GET' and request.cookies.get("auth")):
		token = request.cookies.get('auth')
		print(token)
		payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
		auth = payload['sub']
		print(auth)
		return render_template("dashboard.html", user=auth)
	else:
		error = "You need to login first"
		return render_template("index.html", error=error)

@app.route("/profile", methods=['GET'])
def profile():
	if (request.method == 'GET' and request.cookies.get("auth")):
		token = request.cookies.get('auth')
		payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
		auth = payload['sub']
		return render_template("biodata.html", user=auth)
	else:
		error = "You need to login first"
		return render_template("index.html", error=error)

@app.route("/persyaratan")
def persyaratan():
	if (request.method == 'GET' and request.cookies.get("auth")):
		token = request.cookies.get('auth')
		payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
		auth = payload['sub']
		if (check):
			message = "https://chat.whatsapp.com/CAZ3dVQXOH25NBb823p1HC"
			return render_template("persyaratan.html", message=message, user=auth)
		else:
			return render_template("persyaratan.html", user=auth)
	else:
		error = "You need to login first"
		return render_template("index.html", error=error)

@app.route("/editbiodata")
def edit_bio():
	if (request.method == 'GET' and request.cookies.get("auth")):
		token = request.cookies.get('auth')
		print(token)
		payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
		auth = payload['sub']
		print(auth)
		return render_template("dashboard.html", user=auth)
	else:
		error = "You need to login first"
		return render_template("editbiodata.html", error=error)

@app.route("/logout")
def logout():
	if request.cookies.get('auth'):
		resp = make_response(render_template("index.html"))
		resp.set_cookie('auth', '', expires=0)
		return resp
	else:
		return redirect(url_for('index'))

@app.route("/secret_login")
def secret():
	return render_template("secret_login.html")

@app.route("/secret_dashboard")
def secret_dash():
	return render_template("secret_dashboard.html")