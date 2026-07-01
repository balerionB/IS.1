"""
==========================================================
File: email_service.py

Purpose:
Handles email delivery for the PS-SRMS.

During development, emails are simulated
by printing them to the terminal.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Flask-Mail
# ==========================================================

# Used later for real email delivery.
from flask_mail import Message

# Mail extension.
from app.extensions import mail

# ==========================================================
# Notification Service
# ==========================================================

from app.services.notification_service import (

    mark_as_sent,

    mark_as_failed

)

# ==========================================================
# Send Email
# ==========================================================

def send_email(notification):
    """
    Sends an email notification.

    During development, the email is
    simulated by printing it to the
    terminal.

    Parameters
    ----------
    notification : Notification
        Notification to be delivered.

    Returns
    -------
    bool
        True if successful.
    """

    try:

        # --------------------------------------------------
        # DEVELOPMENT MODE
        # --------------------------------------------------

        print("\n======================================")
        print("SIMULATED EMAIL DELIVERY")
        print("======================================")
        print(f"Recipient : {notification.recipient}")
        print(f"Channel   : {notification.channel}")
        print("Message:")
        print(notification.message)
        print("======================================\n")

        # Mark notification as sent.
        mark_as_sent(notification)

        return True

    except Exception as error:

        print(f"Email Error: {error}")

        # Mark notification as failed.
        mark_as_failed(notification)

        return False
    
"""
# ==========================================================
# Production Email Example
# ==========================================================

message = Message(

    subject="PS-SRMS Notification",

    recipients=[notification.recipient],

    body=notification.message

)

mail.send(message)

mark_as_sent(notification)
"""

# ==========================================================
# Process Pending Emails
# ==========================================================

from app.services.notification_service import (
    get_pending_notifications
)


def process_pending_emails():
    """
    Processes every pending
    EMAIL notification.
    """

    notifications = get_pending_notifications()

    processed = 0

    for notification in notifications:

        if notification.channel == "EMAIL":

            if send_email(notification):

                processed += 1

    print(f"Processed {processed} email notification(s).")

"""
==========================================================
Future Africa's Talking Integration
==========================================================

import africastalking

africastalking.initialize(

    username="YOUR_USERNAME",

    api_key="YOUR_API_KEY"

)

sms = africastalking.SMS

sms.send(

    message=notification.message,

    recipients=[notification.recipient]

)
"""