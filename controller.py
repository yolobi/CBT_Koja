from app import app, bcrypt, jwt
from flask import jsonify, request, redirect, url_for, make_response, render_template, flash
from werkzeug.utils import secure_filename
from db import mysql
from flask_jwt_extended import (create_access_token)
import hashlib
import os
import jwt
import errno
from home import check




@app.route("/api/register", methods=['POST'])
def register_form():
	if request.method == 'POST':
		data = dict(request.form)
		name = data['name']
		email = data['email']
		school = data['school']
		bidang = data['bidang']
		phone = data['nomor']
		password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
		cur = mysql.cursor(buffered=True)
		cur.execute("SELECT 1 FROM users WHERE email=%s", (email,))
		if cur.rowcount == 1:
			print("MasukAAAAAAAa")
			flash("User already exist!")
			return redirect(url_for('register'))
		else:
			cur.execute("INSERT INTO users (name, email, school_address, class, password, phone) VALUES (%s, %s, %s, %s, %s, %s)", (name, email, school, bidang, password, phone))

			mysql.commit()
			cur.close()
			flash('You were successfully registered')
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
		print(rv)
		try:
			if bcrypt.check_password_hash(rv[3], password):
				access_token = create_access_token(identity = {'uid': rv[0],'email': rv[1],'name': rv[2], 'school': rv[4], 'bidang': rv[5], 'phone': rv[6]})
				response = make_response(redirect('/home'))
				response.set_cookie('auth', access_token)
				print(access_token)
				return response
			else:
				flash('Invalid username or password')
				return redirect(url_for("login"))

		except:
			flash('Invalid username or password')
			return redirect(url_for("login"))


@app.route("/api/persyaratan", methods=["POST"])
def upload():
	ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

	def allowed_file(filename):
		return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

	if request.method == 'POST':
		token = request.cookies.get('auth')
		payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
		auth = payload['sub']
		UPLOAD_FOLDER = 'upload/{}'.format(str(auth['uid'])+'_'+auth['name'])
		ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
		app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
		follow = request.files['follow']
		tag_pendaftaran = request.files['tagpendaftaran']
		tag_pembuat = request.files['tagpembuat']
		poster_pendaftaran = request.files['posterpendaftaran']
		poster_pembuat = request.files['posterpembuat']
		share = request.files['share']
		if allowed_file(follow.filename) and allowed_file(tag_pendaftaran.filename) and allowed_file(tag_pembuat.filename) and \
			 allowed_file(poster_pendaftaran.filename) and allowed_file(poster_pembuat.filename) and allowed_file(share.filename):
			try:
				os.mkdir("upload/{}".format(str(auth['uid'])+'_'+auth['name']))
			except OSError as exc:
				if exc.errno != errno.EEXIST:
					raise
				os.system("cd upload ; rm -rf '{}'".format(str(auth['uid'])+'_'+auth['name']))
				os.mkdir("upload/{}".format(str(auth['uid'])+'_'+auth['name']))
			follow_name = secure_filename(follow.filename)
			tag_pendaftaran_name = secure_filename(tag_pendaftaran.filename)
			tag_pembuat_name = secure_filename(tag_pembuat.filename)
			poster_pendaftaran_name = secure_filename(poster_pendaftaran.filename)
			poster_pembuat_name = secure_filename(poster_pembuat.filename)
			share_name = secure_filename(share.filename)
			follow.save(os.path.join(app.config['UPLOAD_FOLDER'], follow_name))
			tag_pendaftaran.save(os.path.join(app.config['UPLOAD_FOLDER'], tag_pendaftaran_name))
			tag_pembuat.save(os.path.join(app.config['UPLOAD_FOLDER'], tag_pembuat_name))
			poster_pendaftaran.save(os.path.join(app.config['UPLOAD_FOLDER'], poster_pendaftaran_name))
			poster_pembuat.save(os.path.join(app.config['UPLOAD_FOLDER'], poster_pembuat_name))
			share.save(os.path.join(app.config['UPLOAD_FOLDER'], share_name))
			message = "https://chat.whatsapp.com/CAZ3dVQXOH25NBb823p1HC"
			check = 1
			return render_template("persyaratan.html", message=message, user=auth)
		else:
			flash("File must be png, jpg, or jpeg")
			return redirect(url_for("persyaratan"))