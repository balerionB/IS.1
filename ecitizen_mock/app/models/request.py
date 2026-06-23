from datetime import datetime

from extensions import db


class CitizenRequest(db.Model):
    """
    Request submitted through eCitizen.
    """

    __tablename__ = "citizen_requests"

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

    citizen_id = db.Column(
        db.Integer,
        db.ForeignKey("citizens.id")
    )

    submitted_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    sync_status = db.Column(
        db.String(50),
        default="PENDING"
    )