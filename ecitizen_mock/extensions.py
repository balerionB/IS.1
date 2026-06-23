# Database ORM.
from flask_sqlalchemy import SQLAlchemy

# Database migrations.
from flask_migrate import Migrate

# JWT Authentication.
from flask_jwt_extended import JWTManager

# Create shared objects.

db = SQLAlchemy()

migrate = Migrate()

jwt = JWTManager()