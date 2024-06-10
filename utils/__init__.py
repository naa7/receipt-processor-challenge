from flask import Blueprint

# Create a Blueprint for the utils module
utils_bp = Blueprint("utils", __name__)

# Import the modules from the utils package
from utils import points_calculator, points_retriever
