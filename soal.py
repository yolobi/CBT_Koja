from flask.templating import render_template_string
from app import app, bcrypt, jwt
from db import mysql
from flask import request, redirect, jsonify, render_template, make_response
import jwt
import json



@app.route("/komputer/<id>", methods=['GET'])
def komputer(id):
    if (request.method == 'GET' and request.cookies.get("auth")):
        token = request.cookies.get('auth')
        payload = jwt.decode(token, app.config.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        auth = payload['sub']
        print(auth['bidang'])
        if auth['bidang'] == 'komputer':
            cur = mysql.cursor(buffered=True)
            cur.execute("SELECT * FROM komputer where id = %s", (id,))
            row_headers = [x[0] for x in cur.description]
            rv = cur.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers,result)))
            res = json.loads(json.dumps(json_data))[0]
            if res['opsi_A'] == res['opsi_B'] == res['opsi_C'] == res['opsi_D'] == res['opsi_E'] == '' and res['kj'] != 'essai':
                return render_template("isian_singkat.html", user=auth, bidang=res)
            else:
                return render_template("pilihan_ganda.html", user=auth, bidang=res)
        else:
            return 'Bidang anda tidak sesuai'
    else:
        error = "You need to login first"
        return render_template("index.html", error=error)