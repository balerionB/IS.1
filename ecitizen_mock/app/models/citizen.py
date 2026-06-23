# Password hashing.
import bcrypt

# Timestamp generation.
from datetime import datetime

# Database object.
from extensions import db


class Citizen(db.Model):
    """
    Represents a citizen
    using the eCitizen portal.
    """

    __tablename__ = "citizens"

    # Primary key.
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # National ID number.
    national_id = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    # Full name.
    full_name = db.Column(
        db.String(255),
        nullable=False
    )

    # Email.
    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    # Phone number.
    phone = db.Column(
        db.String(20)
    )

    # Password hash.
    password_hash = db.Column(
        db.String(255)
    )

    # Account creation date.
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def set_password(self, password):
        """
        Hash password before storage.
        """

        self.password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, password):
        """
        Verify password.
        """

        return bcrypt.checkpw(
            password.encode("utf-8"),
            self.password_hash.encode("utf-8")
        )