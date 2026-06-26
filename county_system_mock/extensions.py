# ==========================================
# extensions.py
#
# Shared Flask extension objects.
# They are initialized later in create_app().
# ==========================================

# SQLAlchemy ORM
from flask_sqlalchemy import SQLAlchemy

# Database migrations
from flask_migrate import Migrate

# JWT authentication
from flask_jwt_extended import JWTManager

# Create shared objects.
# These should only be initialized once.

db = SQLAlchemy()

migrate = Migrate()

jwt = JWTManager()