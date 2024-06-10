from datetime import datetime
import math


def calculate_points(receipt):
    """
    Calculates points for a given receipt.

    This function calculates the points based on various attributes of the receipt,
    including the retailer name, total amount, number of items, item descriptions,
    purchase date, and purchase time.

    Parameters:
    - receipt (dict): A dictionary representing the receipt.

    Returns:
    - points (int): The total points calculated for the receipt.
    """
    points = 0

    # Calculate points based on retailer name
    retailer = receipt.get("retailer")
    for char in retailer:
        points += char.isalnum()

    # Calculate points based on total amount
    total = float(receipt.get("total"))
    if total.is_integer():
        points += 50
    if total % 0.25 == 0:
        points += 25

    # Calculate points based on number of items
    items = receipt.get("items")
    points += (len(items) // 2) * 5

    # Calculate points based on item descriptions and prices
    for item in items:
        item_description = item.get("shortDescription").strip()
        if len(item_description) % 3 == 0:
            price = float(item.get("price"))
            points += math.ceil(price * 0.2)

    # Calculate points based on purchase date
    purchase_date = datetime.strptime(receipt.get("purchaseDate"), "%Y-%m-%d")
    if purchase_date.day % 2 == 1:
        points += 6

    # Calculate points based on purchase time
    purchase_time = datetime.strptime(receipt.get("purchaseTime"), "%H:%M")
    if 14 <= purchase_time.hour <= 16:
        points += 10

    return points
