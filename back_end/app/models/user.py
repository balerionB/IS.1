# Import datetime for timestamps.
from datetime import datetime

# Import database object.
from back_end.app.extensions import db


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
        nullable=False,
        default='citizen'
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
    def set_password(self, password):
        """
        Converts plain text password
        into secure hash.
        """

        self.password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")


    def check_password(self, password):
        """
        Compares entered password
        with stored hash.
        """

        return bcrypt.checkpw(
            password.encode("utf-8"),
            self.password_hash.encode("utf-8")
        )

# Used for password hashing.
import bcrypt

notifications = db.relationship(

    "Notification",

    back_populates="user",

    lazy=True

)
audit_logs = db.relationship(
    "AuditLog",
    back_populates="user",
    lazy=True
)