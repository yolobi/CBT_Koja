from app import app, bcrypt
from db import mysql
from flask import request, redirect, jsonify, render_template
import json
import jwt


@app.route('/admin/page', methods=['GET'])
def page():
	return render_template('admin.html')
