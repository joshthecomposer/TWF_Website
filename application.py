from flask_app import application
from flask_app.controllers import controller
from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    application.run(debug=True)