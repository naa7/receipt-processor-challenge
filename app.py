from flask import Flask
from routes import routes_bp
import logging

# Create a Flask app
app = Flask(__name__)

# Register the routes blueprint
app.register_blueprint(routes_bp, url_prefix="/receipts")

# Set the logging level
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
