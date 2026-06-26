"""
county_manager.py

Represents a county employee who can process
citizen requests.
"""

# Password hashing library
import bcrypt

# Date utilities
from datetime import datetime

# SQLAlchemy instance
from extensions import db


class CountyManager(db.Model):
    """
    Represents authenticated county personnel.
    """

    # Database table name
    __tablename__ = "county_managers"

    # Primary Key
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Full employee name
    full_name = db.Column(
        db.String(150),
        nullable=False
    )

    # Email used during login
    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    # Employee phone number
    phone = db.Column(
        db.String(20)
    )

    # Department
    department = db.Column(
        db.String(100),
        nullable=False
    )

    # Position
    role = db.Column(
        db.String(50),
        nullable=False
    )

    # Password hash
    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    # Account status
    is_active = db.Column(
        db.Boolean,
        default=True
    )

    # Record creation date
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def set_password(self, password):
        """
        Hash the password before saving.
        """

        self.password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, password):
        """
        Verify entered password.
        """

        return bcrypt.checkpw(
            password.encode("utf-8"),
            self.password_hash.encode("utf-8")
        )