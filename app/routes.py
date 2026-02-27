"""
API route definitions.

This module defines HTTP endpoints for user-related operations.
"""
# Import Blueprint to organize routes modularly
from flask import Blueprint, jsonify

# Create Blueprint instance
# name="users" → logical name
# __name__ → module name
user_bp = Blueprint('users', __name__)
@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Endpoint to retrieve a list of users.

    Returns:
        JSON response containing a list of user objects.
    """
    # Sample data representing users
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]
    # Return JSON response with user data
    return jsonify(users)
