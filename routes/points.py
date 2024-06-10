from flask import jsonify
from routes import routes_bp
from utils.points_retriever import retrieve_points


@routes_bp.route("/<id>/points", methods=["GET"])
def get_points(id):
    """
    Retrieves points for a given receipt ID.

    This function retrieves the points associated with the specified receipt ID
    using the `retrieve_points` function from the `utils` module. If the points
    are found, it returns a JSON response containing the points with a status
    code of 200 (OK); otherwise, it returns an error message indicating
    that the receipt was not found with a status code of 404 (Not Found).

    Parameters:
    - id (str): The ID of the receipt.

    Returns:
    - If the points are found, returns a JSON response containing the points
      with a status code of 200 (OK).
    - If the receipt is not found, returns an error message
      indicating that the receipt was not found with a status code of 404 (Not Found).

    Raises:
    - Exception: If an unexpected error occurs during the processing of the receipt.
    """
    try:
        points = retrieve_points(id)
        if points is None:
            return jsonify({"error": "Receipt not found"}), 404
        return jsonify({"points": points}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500
