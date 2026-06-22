# Import database object.
from app.extensions import db


class Department(db.Model):
    """
    Represents a county department.

    Example:
    - Licensing
    - Trade
    - Revenue
    """

    # Database table name.
    __tablename__ = "departments"

    # Primary key.
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Department name.
    name = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    # Department description.
    description = db.Column(
        db.Text
    )

    # Relationship.

    # One department can own many requests.
    service_requests = db.relationship(
        "ServiceRequest",
        back_populates="department"
    )