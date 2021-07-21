from flask.templating import render_template_string
from app import app, bcrypt, jwt, cache
from db import mysql
from flask import request, redirect, jsonify, render_template, make_response
import jwt
import json



@app.route("/komputer/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def komputer(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'komputer'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'komputer':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from komputer")
            total = len(cur.fetchall())
            cur.execute("SELECT * FROM komputer where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/matematika/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def matematika(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'matematika'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'matematika':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from matematika")
            total = len(cur.fetchall())
            print(total)
            cur.execute("SELECT * FROM matematika where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/biologi/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def biologi(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'biologi'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'biologi':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from biologi")
            total = len(cur.fetchall())
            cur.execute("SELECT * FROM biologi where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)
    
@app.route("/kimia/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def kimia(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'kimia'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'kimia':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from kimia")
            total = len(cur.fetchall())
            cur.execute("SELECT * FROM kimia where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/astronomi/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def astronomi(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'astronomi'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'astronomi':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from astronomi")
            total = len(cur.fetchall())
            cur.execute("SELECT * FROM astronomi where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/fisika/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def fisika(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'fisika'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'fisika':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from fisika")
            total = len(cur.fetchall())
            cur.execute("SELECT * FROM fisika where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/ekonomi/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def ekonomi(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'ekonomi'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'ekonomi':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from ekonomi")
            total = len(cur.fetchall())
            cur.execute("SELECT * FROM ekonomi where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)

@app.route("/geografi/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def geografi(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'geografi'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'geografi':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from geografi")
            total = len(cur.fetchall())
            cur.execute("SELECT * FROM geografi where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/kebumian/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def kebumian(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        matkul = 'kebumian'
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'kebumian':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT id from kebumian")
            total = len(cur.fetchall())
            cur.execute("SELECT * FROM kebumian where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/<bidang>/finish")
def finish_attempt(bidang):
    token = request.cookies.get('auth')
    payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
    auth = payload['sub']
    if auth['bidang'] != bidang:
        return 'Bidang anda tidak sesuai'
    return render_template("finish.html")

@app.route("/<bidang>/essay")
def upload_essay(bidang):
    return render_template("essay.html")