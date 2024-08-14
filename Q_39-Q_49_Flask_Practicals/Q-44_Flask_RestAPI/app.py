

# Q44.How would you create a RESTful API endpoint in Flask that returns JSON data?

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import User  # Import the User model

@app.route('/')
def index():
    return 'Welcome to the Flask API!'

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })
    return jsonify(users_list)

if __name__ == '__main__':
    app.run(debug=True)
