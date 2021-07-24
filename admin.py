from flask.helpers import url_for
from app import app, bcrypt
import db
from flask import request, redirect, jsonify, render_template, flash
import json
import jwt


@app.route('/admin/1c096d6e413c588e44cb9031d03b012f', methods=['GET'])
def admin_page():
	return render_template('upload_soal.html')

@app.route("/admin/bio")
def admin_bio():
	return render_template("upload_bio.html")

@app.route("/api/bio", methods=['POST'])
def add_bio():
	if request.method == 'POST':
		mysql = db.connect()
		data = dict(request.form)
		soal = data['soal'].replace('\r\n', '')
		nomor = data['no_soal']
		q1 = data['q1'].replace('\r\n', '')
		q2 = data['q2'].replace('\r\n', '')
		q3 = data['q3'].replace('\r\n', '')
		q4 = data['q4'].replace('\r\n', '')
		a1 = data['a1']
		a2 = data['a2']
		a3 = data['a3']
		a4 = data['a4']
		point = data['point']
		cur = mysql.cursor()
		cur.execute("INSERT INTO `biologi` (id, soal, q1, q2, q3, q4, a1, a2, a3, a4, point) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, q1, q2, q3, q4, a1, a2, a3, a4, point))
		mysql.commit()
		cur.close()
		mysql.close()
		msg = "Success added soal {} no {}".format('biologi', nomor)
		flash(msg)
		return redirect(url_for('admin_bio'))

@app.route("/api/soal", methods=["POST"])
def add_soal():
	mysql = db.connect()
	if request.method == 'POST':
		cur = mysql.cursor()
		data = dict(request.form)
		bidang = data['bidang']
		nomor = data['no_soal']
		soal = data['soal'].replace('\r\n', '')
		opsi_a = data['opsi_a'].replace('\r\n', '')
		opsi_b = data['opsi_b'].replace('\r\n', '')
		opsi_c = data['opsi_c'].replace('\r\n', '')
		opsi_d = data['opsi_d'].replace('\r\n', '')
		opsi_e = data['opsi_e'].replace('\r\n', '')
		point = data['bobot']
		kj = data['kunci'].lower()
		print(data)
		if bidang == 'matematika':
			cur.execute("INSERT INTO `matematika` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'biologi':
			cur.execute("INSERT INTO `biologi` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'fisika':
			cur.execute("INSERT INTO `fisika` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'kimia':
			cur.execute("INSERT INTO `kimia` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'komputer':
			cur.execute("INSERT INTO `komputer` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'astronomi':
			cur.execute("INSERT INTO `astronomi` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'geografi':
			cur.execute("INSERT INTO `geografi` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'kebumian':
			cur.execute("INSERT INTO `kebumian` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'ekonomi':
			cur.execute("INSERT INTO `ekonomi` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		elif bidang == 'ujicoba':
			cur.execute("INSERT INTO `ujicoba` (id, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, point, kj))
		mysql.commit()
		cur.close()
		msg = "Success added soal {} no {}".format(bidang, 	nomor)
		flash(msg)
		return redirect(url_for('admin_page'))