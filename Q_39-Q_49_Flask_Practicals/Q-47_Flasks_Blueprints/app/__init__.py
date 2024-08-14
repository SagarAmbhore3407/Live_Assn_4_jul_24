
from flask import Flask
from app.blueprints import my_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(my_blueprint, url_prefix='/my')
    return app

