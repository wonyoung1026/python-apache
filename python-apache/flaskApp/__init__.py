from flask import Flask
from flask_cors import CORS


app = Flask(__name__, static_url_path='')
CORS(app)

from flaskApp.routes import index