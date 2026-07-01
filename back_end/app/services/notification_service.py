"""
==========================================================
File: notification_service.py

Purpose:
Handles all notification operations
for the PS-SRMS.

Responsibilities:
1. Create notifications.
2. Retrieve pending notifications.
3. Mark notifications as sent.
4. Mark notifications as failed.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Standard Library
# ==========================================================

# Used for recording the time a notification is sent.
from datetime import datetime

# ==========================================================
# Database
# ==========================================================

from app.extensions import db

# ==========================================================
# Notification Model
# ==========================================================

from app.models.notification import Notification

# ==========================================================
# Create Notification
# ==========================================================

def create_notification(
    request_id,
    recipient,
    channel,
    message
):
    """
    Creates a new notification.

    Parameters
    ----------
    request_id : int
        Related service request.

    recipient : str
        Email address or phone number.

    channel : str
        EMAIL or SMS.

    message : str
        Notification message.

    Returns
    -------
    Notification
        Newly created notification.
    """

    # Create a notification object.
    notification = Notification(

        request_id=request_id,

        recipient=recipient,

        channel=channel,

        message=message,

        status="PENDING"

    )

    # Save to database.
    db.session.add(notification)

    db.session.commit()

    return notification

# ==========================================================
# Retrieve Pending Notifications
# ==========================================================

def get_pending_notifications():
    """
    Returns every notification
    waiting to be sent.
    """

    return Notification.query.filter_by(

        status="PENDING"

    ).all()

# ==========================================================
# Mark Notification as Sent
# ==========================================================

def mark_as_sent(notification):
    """
    Updates a notification after
    successful delivery.
    """

    notification.status = "SENT"

    notification.sent_at = datetime.utcnow()

    db.session.commit()

# ==========================================================
# Mark Notification as Failed
# ==========================================================

def mark_as_failed(notification):
    """
    Updates a notification if
    delivery fails.
    """

    notification.status = "FAILED"

    db.session.commit()    