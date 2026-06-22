# Import required modules
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create a new FastAPI app
app = FastAPI()

# Define CORS policy
origins = [
    "http://localhost:3000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import routes
from routes import order_routes, restaurant_routes, item_routes, user_routes

# Include routes in the app
app.include_router(order_routes)
app.include_router(restaurant_routes)
app.include_router(item_routes)
app.include_router(user_routes)
