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

from app.auth.routes import auth_bp
from app.integrations.routes import integration_bp
from app.dashboard.routes import dashboard_bp
from app.ecitizen.routes import ecitizen_bp
from app.county.routes import county_bp


# ==========================================================
# Application Factory
# ==========================================================

def create_app():
    """
    Creates and configures
    the Flask application.
    """

    app = Flask(
        __name__,
        template_folder="../../frontend/templates",
        static_folder="../../frontend/static"
    )

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)

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

    return app
