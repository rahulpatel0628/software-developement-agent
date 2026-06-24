from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from database import db
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/dbname'
db = SQLAlchemy(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404