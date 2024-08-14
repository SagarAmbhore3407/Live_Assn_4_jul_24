

#Q43. Describe the process of connecting a Flask app to a SQLite database using SQLAlchemy.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import User  # Ensure this is correct

@app.route('/')
def index():
    return 'Welcome to the Flask App with SQLAlchemy!'

if __name__ == '__main__':
    app.run(debug=True)
