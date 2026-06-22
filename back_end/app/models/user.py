# Import datetime for timestamps.
from datetime import datetime

# Import database object.
from app.extensions import db


class User(db.Model):
    """
    Represents authenticated users
    of the governance platform.
    """

    __tablename__ = "users"

    # Unique identifier.
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Full name.
    name = db.Column(
        db.String(100),
        nullable=False
    )

    # Email address.
    email = db.Column(
        db.String(120),
        nullable=False,
        unique=True
    )

    # Phone number.
    phone = db.Column(
        db.String(20)
    )

    # Role.

    # SUPERVISOR
    # OVERSIGHT
    # MANAGER
    # CITIZEN
    # SYSTEM
    role = db.Column(
        db.String(30),
        nullable=False
    )

    # Password hash.

    # Never store passwords directly.
    password_hash = db.Column(
        db.String(255)
    )

    # Whether account is active.
    is_active = db.Column(
        db.Boolean,
        default=True
    )

    # Creation timestamp.
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )