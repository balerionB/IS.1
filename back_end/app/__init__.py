# Import Flask class.
from flask import Flask

# Import extensions created earlier.
from app.extensions import db, migrate, jwt, mail

from app.auth.routes import auth_bp
from app.integrations.routes import (
    integration_bp
)
from app.dashboard.routes import dashboard_bp

# Application Factory Pattern.
# Creates and configures the Flask application.
def create_app():

    # Create Flask application object.
    app = Flask(
        __name__,
        template_folder="../../frontend/templates",
        static_folder="../../frontend/static"
    )

    # Load configurations from config.py.
    app.config.from_object("config.Config")

    # Initialize SQLAlchemy.
    db.init_app(app)

    # Initialize migrations.
    migrate.init_app(app, db)

    # Initialize JWT authentication.
    jwt.init_app(app)

    # Initialize mail service.
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
        dashboard_bp
    )

    # Return configured application.
    return app
