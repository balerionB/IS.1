# Import datetime for timestamps.
from datetime import datetime

# Import database object.
from app.extensions import db


class RequestStatusHistory(db.Model):
    """
    Tracks every state transition
    of a service request.
    """

    __tablename__ = "request_status_history"

    # Primary key.
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Foreign key to request.
    request_id = db.Column(
        db.Integer,
        db.ForeignKey("service_requests.id"),
        nullable=False
    )

    # Previous state.
    old_status = db.Column(
        db.String(50)
    )

    # New state.
    new_status = db.Column(
        db.String(50),
        nullable=False
    )

    # User responsible.
    #
    # Can be NULL if SYSTEM initiated.
    changed_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=True
    )

    # Actor role.
    #
    # Examples:
    # CITIZEN
    # MANAGER
    # SYSTEM
    # EXTERNAL_SYSTEM
    actor_role = db.Column(
        db.String(50),
        nullable=False
    )

    # Reason for change.
    reason = db.Column(
        db.Text
    )

    # Timestamp.
    changed_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationship back to request.
    request = db.relationship(
        "ServiceRequest",
        backref="status_history"
    )