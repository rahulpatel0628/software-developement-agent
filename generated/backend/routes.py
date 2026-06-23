from flask import Flask, request, jsonify
from database import Session
from models import User

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    session = Session()
    users = session.query(User).all()
    return jsonify([user.name for user in users])

@app.errorhandler(429)
def rate_limit_exceeded(e):
    return jsonify({'error': 'Rate limit exceeded'}), 429