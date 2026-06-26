# ==========================================
# app.py
#
# Entry point for the County Office System.
# ==========================================

from flask import Flask

from config import Config

from extensions import db, migrate, jwt


def create_app():
    """
    Creates and configures
    the Flask application.
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    return app


# Create application instance
app = create_app()


# Run only when executing directly.
if __name__ == "__main__":
    app.run(debug=True, port=5002)