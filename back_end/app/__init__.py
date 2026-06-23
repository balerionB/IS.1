# Import Flask class.
from flask import Flask

# Import extensions created earlier.
from app.extensions import db, migrate, jwt, mail


# Application Factory Pattern.
# Creates and configures the Flask application.
def create_app():

    # Create Flask application object.
    app = Flask(__name__)

    # Load configurations from config.py.
    app.config.from_object("app.config.Config")

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

    # Return configured application.
    return app
from app.auth.routes import auth_bp