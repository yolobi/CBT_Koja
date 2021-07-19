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
		soal = data['soal']
		opsi_a = data['opsi_a'].lower()
		opsi_b = data['opsi_b'].lower()
		opsi_c = data['opsi_c'].lower()
		opsi_d = data['opsi_d'].lower()
		opsi_e = data['opsi_e'].lower()
		point = data['point']
		kj = data['kunci']
		cur.execute("INSERT INTO %s (id, bidang, soal, opsi_A, opsi_B, opsi_C, opsi_D, opsi_E, point, kj) \
		VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (bidang, nomor, soal, opsi_a, opsi_b, opsi_c, opsi_d, opsi_e, kj))
		return '123'