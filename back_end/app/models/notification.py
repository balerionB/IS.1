from datetime import datetime
from app.extensions import db


class Notification(db.Model):

    __tablename__ = "notifications"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    request_id = db.Column(
        db.Integer,
        db.ForeignKey("service_requests.id")
    )

    recipient = db.Column(
        db.String(255),
        nullable=False
    )

    # EMAIL or SMS.
    channel = db.Column(
        db.String(20),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="PENDING"
    )

    sent_at = db.Column(
        db.DateTime
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )