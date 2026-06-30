from datetime import datetime

from back_end.app.extensions import db


class ServiceRequest(db.Model):
    """
    Core governance entity.

    Represents one permit renewal request.
    """

    __tablename__ = "service_requests"

    # Request ID.
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Public reference number.
    reference_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    # Request title.
    title = db.Column(
        db.String(255),
        nullable=False
    )

    # Request details.
    description = db.Column(
        db.Text
    )

    # Current state.
    status = db.Column(
        db.String(50),
        nullable=False,
        default="SUBMITTED"
    )

    # Request creation date.
    submitted_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # SLA deadline.

    # Once set, should never change.
    sla_deadline = db.Column(
        db.DateTime,
        nullable=False
    )

    # Escalation flag.
    is_escalated = db.Column(
        db.Boolean,
        default=False
    )

    # Foreign key.

    department_id = db.Column(
        db.Integer,
        db.ForeignKey("departments.id")
    )

    # Relationship.

    department = db.relationship(
        "Department",
        back_populates="service_requests"
    )
    attachments = db.relationship(

        "Attachment",

        back_populates="request",

        lazy=True,

        cascade="all, delete-orphan"

    )