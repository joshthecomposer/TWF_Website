from flask import Flask
# from flask_cors import CORS

application = Flask(__name__)
application.secret_key = 'secret key'
# CORS(application)
