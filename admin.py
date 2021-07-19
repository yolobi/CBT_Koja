from app import app, bcrypt
from db import mysql
from flask import request, redirect, jsonify, render_template
import json
import jwt


@app.route('/admin/1c096d6e413c588e44cb9031d03b012f', methods=['GET'])
def page():
	return render_template('upload_soal.html')


@app.route("/api/soal", methods=["POST"])
def add_soal():
	if request.method == 'POST':
		cur = cur = mysql.cursor(buffered=True)
		data = dict(request.form)
		bidang = data['bidang']
		nomor = data['no_soal']
		soal = data['soal'].replace('\r\n', '')
		opsi_a = data['opsi_a'].lower()
		opsi_b = data['opsi_b'].lower()
		opsi_c = data['opsi_c'].lower()
		opsi_d = data['opsi_d'].lower()
		opsi_e = data['opsi_e'].lower()
		point = data['bobot']
		kj = data['kunci']
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
		mysql.commit()
		cur.close()
		return '123'