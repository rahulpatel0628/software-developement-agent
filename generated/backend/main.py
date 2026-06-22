from flask import Flask
from routes import order_routes, restaurant_routes, item_routes, user_routes
app = Flask(__name__)
app.register_blueprint(order_routes)
app.register_blueprint(restaurant_routes)
app.register_blueprint(item_routes)
app.register_blueprint(user_routes)
if __name__ == '__main__':
    app.run(debug=True)