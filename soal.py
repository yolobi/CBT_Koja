from flask.wrappers import Response
from controller import reset
import re
from flask.helpers import url_for
from flask.templating import render_template_string
from app import app, bcrypt, jwt, cache
from db import mysql
from flask import request, redirect, jsonify, render_template, make_response, flash
import jwt
import json
import datetime
import time

total_soal = {
    'matematika': 20,
    'komputer': 40,
    'fisika': 7,
    'kebumian': 45,
    'astronomi': 7,
    'ekonomi': 55,
    'kimia': 90,
    'geografi': 55,
    'biologi': 50,
}

def create_timer(uid):
	token = jwt.encode({"uid": uid, "exp": datetime.datetime.now() + datetime.timedelta(seconds=30000)}, app.config.get('JWT_SECRET_KEY'))
	return token

def decode_jwt(token):
    res = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
    return res


@app.route("/start/1c096d6e413c588e44cb9031d03b012f")
def start():
    cur = mysql.cursor(buffered=True)
    id = 1
    token = request.cookies.get('auth')
    payload = decode_jwt(token)
    auth = payload['sub']
    #check session
    cur = mysql.cursor(buffered=True)
    cur.execute("select session from users where uid = %s", (auth['uid'],))
    rv = cur.fetchone()
    print(rv)
    if (rv[0]):
        return 'Session anda telah habis'
    if (request.cookies.get("session")):
        return redirect(url_for('{}'.format(auth['bidang']),id=id))
    response = make_response(redirect(url_for('{}'.format(auth['bidang']), id=id)))
    session = create_timer(auth['uid'])
    response.set_cookie('session', session)
    print(session)
    return response

@app.route("/komputer/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def komputer(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'komputer':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            cur.execute("SELECT * FROM komputer where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/matematika/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def matematika(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'matematika':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            print(total)
            cur.execute("SELECT * FROM matematika where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return redirect(url_for('home'))


@app.route("/biologi/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def biologi(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'biologi':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            cur.execute("SELECT * FROM biologi where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)
    
@app.route("/kimia/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def kimia(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'kimia':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            cur.execute("SELECT * FROM kimia where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/astronomi/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def astronomi(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'astronomi':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            cur.execute("SELECT * FROM astronomi where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/fisika/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def fisika(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'fisika':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            cur.execute("SELECT * FROM fisika where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/ekonomi/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def ekonomi(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'ekonomi':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            cur.execute("SELECT * FROM ekonomi where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)

@app.route("/geografi/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def geografi(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'geografi':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            cur.execute("SELECT * FROM geografi where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/kebumian/1c096d6e413c588e44cb9031d03b012f/<id>", methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def kebumian(id):
    if (request.method == 'GET' and request.cookies.get("auth") and request.cookies.get("session")):
        token = request.cookies.get('auth')
        session = request.cookies.get('session')
        payload = decode_jwt(token)
        auth = payload['sub']
        try:
            timer = decode_jwt(session)
        except:
            return redirect(url_for('finish_attempt',bidang=auth['bidang']))
        if auth['bidang'] == 'kebumian':
            cur = mysql.cursor(buffered=True)
            total = total_soal[auth['bidang']]
            cur.execute("SELECT * FROM kebumian where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['kj'] == 'essay' or res['kj'] == 'essai':
                return render_template("soal_essai.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            elif res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '':
                return render_template("isian_singkat.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res, len=total, timer=timer['exp']*1000)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)


@app.route("/<bidang>/finish")
@cache.cached(timeout=10, query_string=True)
def finish_attempt(bidang):
    cur = mysql.cursor(buffered=True)
    token = request.cookies.get('auth')
    payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
    auth = payload['sub']
    if auth['bidang'] != bidang:
        return 'Bidang anda tidak sesuai'
    cur.execute("select session from users where uid = %s", (auth['uid'],))
    rv = cur.fetchone()
    if(rv[0]):
        return 'Session Anda telah habis'
    total = total_soal[bidang]
    return render_template("finish.html", user=auth, len=total)

@app.route("/<bidang>/essay")
def upload_essay(bidang):
    token = request.cookies.get('auth')
    payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
    auth = payload['sub']
    if auth['bidang'] != bidang:
        return 'Bidang anda tidak sesuai'
    total = total_soal[bidang]
    return render_template("essay.html", user=auth, len=total)


@app.route("/api/send", methods=['POST'])
def finish_post():
    if request.method == 'POST':
        token = request.cookies.get('auth')
        payload = decode_jwt(token)
        auth = payload['sub']
        cur = mysql.cursor(buffered=True)
        cur.execute("UPDATE users SET session = TRUE where uid = %s", (auth['uid'],))
        mysql.commit()
        data = dict(request.form)
        print(data)
        date = (time.strftime('%Y-%m-%d %H:%M:%S'))
        for i in range(len(data)):
            cur.execute("INSERT INTO history (uid, answer, submitted_at) VALUES (%s, %s, %s)", (auth['uid'], data[str(i+1)], date))
            mysql.commit()
        flash("Jawaban Anda berhasil tersimpan, terimakasih")
        resp = make_response(redirect(url_for("home")))
        resp.set_cookie('session', '', expires=0)
        return resp