from flask import jsonify, request, current_app
from routes import routes_bp
from utils.points_calculator import calculate_points
from app_state import AppState
import uuid


@routes_bp.route("/process", methods=["POST"])
def process_receipt():
    """
    Processes a receipt and returns the receipt ID.

    This function receives a JSON object representing a receipt in the request body.
    It generates a unique ID for the receipt, calculates the points for the receipt
    using the `calculate_points function` from the `utils` module, and stores the 
    receipt ID and points in the app_state singleton instance.

    JSON Request Body:
    {
        "receipt": {
            "retailer": "Retailer Name",
            "total": 100.50,
            "purchaseDate": "2024-06-01",
            "purchaseTime": "15:30",
            "items": [
                {
                    "shortDescription": "Item 1",
                    "price": 50.25
                },
                {
                    "shortDescription": "Item 2",
                    "price": 50.25
                }
            ]
        }
    }

    Returns:
    - If processing is successful, returns a JSON response containing the receipt ID
      with a status code of 200 (OK).

    Raises:
    - Exception: If an unexpected error occurs during the processing of the receipt.
    """
    try:
        receipt = request.json
        receipt_id = str(uuid.uuid4())

        app_state = AppState()
        receipt_points = calculate_points(receipt)

        app_state.receipts[receipt_id] = receipt_points
        # current_app.logger.info(f"Current receipts stored: {app_state.receipts}")

        return jsonify({"id": receipt_id}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500
