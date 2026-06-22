from datetime import datetime
from app.extensions import db


class OfficerNote(db.Model):

    __tablename__ = "officer_notes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    request_id = db.Column(
        db.Integer,
        db.ForeignKey("service_requests.id"),
        nullable=False
    )

    note = db.Column(
        db.Text,
        nullable=False
    )

    # False = visible to citizen.
    # True = internal note.
    is_internal = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )