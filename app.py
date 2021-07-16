from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_mail import Mail



app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config['JWT_SECRET_KEY'] = '_5#y2L"F4Q8z\n\xec]/'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=3)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#mail
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'riyanti.hersal@gmail.com'
app.config['MAIL_PASSWORD'] = 'Greyabuabu201!'

mail = Mail(app)
jwt = JWTManager(app)