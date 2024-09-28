from flask import Flask
from .routes import routes
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    app.config.from_pyfile('../instance/config.py')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.register_blueprint(routes)
    return app
