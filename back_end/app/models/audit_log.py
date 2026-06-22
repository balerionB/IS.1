# Import datetime.
from datetime import datetime

# Import database object.
from app.extensions import db


class AuditLog(db.Model):
    """
    Tamper-evident audit trail.

    Stores snapshots before and
    after every database change.
    """

    __tablename__ = "audit_log"

    # Primary key.
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # Table affected.
    table_name = db.Column(
        db.String(100),
        nullable=False
    )

    # Record affected.
    record_id = db.Column(
        db.Integer,
        nullable=False
    )

    # INSERT
    # UPDATE
    # DELETE
    operation = db.Column(
        db.String(20),
        nullable=False
    )

    # Source system.
    #
    # COUNTY_SYSTEM
    # ECITIZEN
    # PS_SRMS
    source_system = db.Column(
        db.String(50),
        nullable=False
    )

    # Snapshot before change.
    before_state = db.Column(
        db.JSON
    )

    # Snapshot after change.
    after_state = db.Column(
        db.JSON
    )

    # Creation timestamp.
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )