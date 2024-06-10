from app_state import AppState


def retrieve_points(id):
    """
    Retrieve points for a given receipt ID.

    This function retrieves the points associated with the specified receipt ID
    from the app_state.

    Parameters:
    - id (str): The ID of the receipt.

    Returns:
    - points (int or None): The points associated with the receipt ID,
      or None if the receipt ID is not found.
    """
    app_state = AppState()
    points = app_state.receipts.get(id)
    return points
