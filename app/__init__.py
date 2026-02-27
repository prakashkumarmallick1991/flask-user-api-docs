"""
Application factory module.

This module creates and configures the Flask application.
"""

from flask import Flask
def create_app():
    
     # Create Flask application object
    app = Flask(__name__)
    
      # Import blueprint inside function to avoid circular imports
       # Register blueprint with the main app
    # This attaches all routes defined in routes.py to the Flask application
    from .routes import user_bp
    app.register_blueprint(user_bp)
     # Return configured application
    return app
