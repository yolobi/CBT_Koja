from app import app, bcrypt, jwt
from flask import jsonify, request, redirect, url_for, make_response, render_template, flash
from db import mysql
from flask_jwt_extended import (create_access_token)
import hashlib


@app.route("/api/register", methods=['POST'])
def register_form():
	if request.method == 'POST':
		data = dict(request.form)
		name = data['name']
		email = data['email']
		school = data['school']
		bidang = data['bidang']
		password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
		cur = mysql.cursor(buffered=True)
		cur.execute("SELECT 1 FROM users WHERE email=%s", (email,))
		if cur.rowcount == 1:
			print("MasukAAAAAAAa")
			flash("User already exist!")
			return redirect(url_for('register'))
		else:
			cur.execute("INSERT INTO users (name, email, school_address, class, password) VALUES (%s, %s, %s, %s, %s)", (name, email, school, bidang, password))

			mysql.commit()
			cur.close()
			flash('You were successfully register')
			return redirect(url_for('login'))


@app.route("/api/login", methods=['POST'])
def login_form():
	if request.method == 'POST':
		data = dict(request.form)
		cur = mysql.cursor(buffered=True)
		email = data['email']
		password = data['password']
		result = ""
		
		cur.execute("SELECT * FROM users where email = %s", (email,))
		rv = cur.fetchone()
		try:
			if bcrypt.check_password_hash(rv[3], password):
				access_token = create_access_token(identity = {'uid': rv[0],'email': rv[1],'name': rv[2], 'school': rv[4], 'bidang': rv[5]})
				response = make_response(redirect('/home'))
				response.set_cookie('auth', access_token)
				print(access_token)
				return response
			else:
				result = jsonify({"error":"Invalid username and password"})

			return result


		except Exception as e:
			print(e)
			result = jsonify({"error":"Invalid username and password"})
			return result


@app.route("/api/persyaratan", methods=["POST"])
def upload():
	if request.method == 'POST':
		data = request.files['follow']
		print(data)

		return '123'