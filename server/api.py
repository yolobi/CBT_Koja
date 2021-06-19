from app import app
from home import *
from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")