# Import SQLAlchemy ORM
# This allows Python classes to be mapped to database tables.
from flask_sqlalchemy import SQLAlchemy

# Import migration tool.
# Handles database versioning and schema changes.
from flask_migrate import Migrate

# Import JWT manager.
# Handles authentication tokens.
from flask_jwt_extended import JWTManager

# Import Flask-Mail.
# Handles email notifications.
from flask_mail import Mail


# Create database object.
# This object will be initialized inside create_app().
db = SQLAlchemy()

# Create migration object.
migrate = Migrate()

# Create JWT manager object.
jwt = JWTManager()

# Create mail object.
mail = Mail()