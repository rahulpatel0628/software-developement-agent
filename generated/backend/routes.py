from flask import Blueprint, request, jsonify
from models import User, Restaurant, Order, Item
order_routes = Blueprint('order_routes', __name__)
@order_routes.route('/api/orders', methods=['GET'])
def get_orders():
    orders = Order.objects.all()
    return jsonify([order.to_dict() for order in orders])
restaurant_routes = Blueprint('restaurant_routes', __name__)
@restaurant_routes.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.objects.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])
item_routes = Blueprint('item_routes', __name__)
@item_routes.route('/api/items', methods=['GET'])
def get_items():
    items = Item.objects.all()
    return jsonify([item.to_dict() for item in items])
user_routes = Blueprint('user_routes', __name__)
@user_routes.route('/api/users', methods=['GET'])
def get_users():
    users = User.objects.all()
    return jsonify([user.to_dict() for user in users])