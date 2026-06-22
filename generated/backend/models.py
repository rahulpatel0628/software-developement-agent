from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client['DeliveryApp']
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
class Restaurant:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
class Order:
    def __init__(self, id, user_id, restaurant_id, status):
        self.id = id
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.status = status
class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price