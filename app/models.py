"""
Data models for the application.

This file defines business domain objects.
"""
class User:
    """
    Represents a user entity.

    Attributes:
        id (int): Unique identifier of the user
        name (str): Full name of the user
        email (str): Email address of the user
    """
    def __init__(self, id, name, email):
            """
        Initialize a User object.

        Args:
            id (int): Unique user ID
            name (str): User's full name
            email (str): User's email address
        """
         # Assign values to instance variables
            self.id = id
            self.name = name
            self.email = email
         