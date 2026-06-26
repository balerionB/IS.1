"""
request.py

Represents requests received
from PS-SRMS.
"""

from datetime import datetime

from extensions import db


class CountyRequest(db.Model):

    __tablename__ = "county_requests"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    reference_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    title = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(50),
        default="SUBMITTED"
    )

    assigned_to = db.Column(
        db.Integer,
        db.ForeignKey("county_managers.id")
    )

    received_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    # ---------------------------------------------------------
    # Relationship to CountyManager
    #
    # This allows us to access the assigned manager directly.
    # Example:
    # request.manager.full_name
    # ---------------------------------------------------------

    manager = db.relationship(
        "CountyManager",
        backref="assigned_requests"
    )
