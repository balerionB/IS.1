from datetime import datetime
from app.extensions import db


class Attachment(db.Model):

    __tablename__ = "request_attachments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    request_id = db.Column(
        db.Integer,
        db.ForeignKey("service_requests.id"),
        nullable=False
    )

    file_name = db.Column(
        db.String(255),
        nullable=False
    )

    # AWS S3 object key.
    s3_key = db.Column(
        db.String(500),
        nullable=False
    )

    signed_url = db.Column(
        db.Text
    )

    url_expiry = db.Column(
        db.DateTime
    )

    uploaded_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )