from flask import Blueprint

# Create a Blueprint for the routes
routes_bp = Blueprint("routes", __name__)

# Import the modules from the routes package
from routes import process, points
