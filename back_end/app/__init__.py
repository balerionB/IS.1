"""
==========================================================
File: __init__.py

Purpose:
Creates and configures the
Flask application.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Flask
# ==========================================================

from flask import Flask

# ==========================================================
# Extensions
# ==========================================================

from app.extensions import (
    db,
    migrate,
    jwt,
    mail
)

# ==========================================================
# Blueprints
# ==========================================================

# Authentication routes.
from app.auth.routes import auth_bp

# Integration routes.
from app.integrations.routes import integration_bp

# Dashboard routes.
from app.dashboard.routes import dashboard_bp

# Simulated eCitizen routes.
from app.ecitizen.routes import ecitizen_bp

# Simulated County Office routes.
from app.county.routes import county_bp


# ==========================================================
# Application Factory
# ==========================================================

def create_app():
    """
    Creates and configures
    the Flask application.
    """

    # Create Flask application.
    app = Flask(__name__)

    # Load configuration.
    app.config.from_object("config.Config")

    # Initialize extensions.
    db.init_app(app)

    migrate.init_app(
        app,
        db
    )

    jwt.init_app(app)

    mail.init_app(app)

    # ------------------------------------------------------
    # Register application blueprints.
    # ------------------------------------------------------

    app.register_blueprint(
        auth_bp,
        url_prefix="/api/auth"
    )

    app.register_blueprint(
        integration_bp,
        url_prefix="/api/integrations"
    )

    app.register_blueprint(
        dashboard_bp,
        url_prefix="/api/dashboard"
    )

    app.register_blueprint(
        ecitizen_bp,
        url_prefix="/api/ecitizen"
    )

    app.register_blueprint(
        county_bp,
        url_prefix="/api/county"
    )

    # Return configured application.
    return app