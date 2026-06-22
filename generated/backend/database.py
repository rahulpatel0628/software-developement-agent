# Import required modules
from pymongo import MongoClient

# Create a new MongoDB client
client = MongoClient('mongodb://localhost:27017/')

# Create a new database
db = client['delivery_app']
