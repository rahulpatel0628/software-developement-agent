# Import required modules
from pydantic import BaseModel

# Define the User model
class User(BaseModel):
    id: str
    name: str
    email: str

# Define the Restaurant model
class Restaurant(BaseModel):
    id: str
    name: str
    address: str

# Define the Item model
class Item(BaseModel):
    id: str
    name: str
    price: float

# Define the Order model
class Order(BaseModel):
    id: str
    user_id: str
    restaurant_id: str
    status: str
