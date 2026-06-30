from datetime import datetime
from app import db


class Attachment(db.Model):

    __tablename__ = "attachments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    request_id = db.Column(
        db.Integer,
        db.ForeignKey("service_requests.id"),
        nullable=False
    )

    uploaded_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    file_name = db.Column(
        db.String(255),
        nullable=False
    )

    s3_key = db.Column(
        db.String(500),
        nullable=False
    )

    content_type = db.Column(
        db.String(100)
    )

    file_size = db.Column(
        db.BigInteger
    )

    uploaded_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    request = db.relationship(
        "ServiceRequest",
        back_populates="attachments"
    )

    user = db.relationship(
        "User"
    )