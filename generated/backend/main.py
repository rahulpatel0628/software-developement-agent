import logging
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from database import db
from routes import main_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

db.init_app(app)

app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)