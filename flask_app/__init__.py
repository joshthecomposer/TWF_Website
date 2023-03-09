from flask import Flask
from os import environ
from flask_cors import CORS


application = Flask(__name__)
application.secret_key = environ.get('SECRET_KEY')
application.DB_HOST = environ.get("DB_HOST")
application.DB_USER = environ.get("DB_USER")
application.DB_PASS = environ.get("DB_PASS")
application.DB_PORT = environ.get("DB_PORT")
CORS(application)