from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta



app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config['JWT_SECRET_KEY'] = 'secret'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=3)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
jwt = JWTManager(app)