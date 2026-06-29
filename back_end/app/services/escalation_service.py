"""
==========================================================
File: escalation_service.py

Purpose:
Handles automatic SLA escalations.

This service is responsible for:
1. Checking if a request has breached its SLA.
2. Updating the request status to ESCALATED.
3. Recording the status change.
4. Creating a notification.
5. Saving all changes to the database.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Database instance
# ==========================================================

# Used to save changes to the database.
from app.extensions import db

# ==========================================================
# Models
# ==========================================================

# Main Service Request model.
from app.models.service_request import ServiceRequest

# Stores every workflow status transition.
from app.models.request_status_history import (
    RequestStatusHistory
)

# Stores notifications for users.
from app.models.notification import Notification

# ==========================================================
# SLA Helper Functions
# ==========================================================

# Function that checks whether a request
# has exceeded its SLA.
from app.services.sla_service import (
    is_sla_breached
)


# ==========================================================
# Escalate a Single Request
# ==========================================================

def escalate_request(request):
    """
    Escalates a request that has exceeded its SLA.

    Parameters
    ----------
    request : ServiceRequest
        The request object to be escalated.

    Returns
    -------
    bool
        True if the request was escalated successfully.
        False otherwise.
    """

    # ------------------------------------------------------
    # Prevent duplicate escalations.
    # If the request has already been escalated,
    # do nothing.
    # ------------------------------------------------------

    if request.status == "ESCALATED":

        return False

    # ------------------------------------------------------
    # Check whether the SLA has actually been breached.
    # If not, there is nothing to do.
    # ------------------------------------------------------

    if not is_sla_breached(request.created_at):

        return False

    # ------------------------------------------------------
    # Store the previous workflow status.
    # This will be recorded in the history table.
    # ------------------------------------------------------

    previous_status = request.status

    # ------------------------------------------------------
    # Update the request status.
    # ------------------------------------------------------

    request.status = "ESCALATED"

    # ------------------------------------------------------
    # Save the updated request.
    # ------------------------------------------------------

    db.session.commit()

    # ------------------------------------------------------
    # Create a workflow history record.
    # This keeps track of every status change.
    # ------------------------------------------------------

    history = RequestStatusHistory(

        request_id=request.id,

        old_status=previous_status,

        new_status="ESCALATED",

        changed_by=None,

        actor_role="SYSTEM",

        reason="Automatic SLA Escalation"

    )

    # Add history record to the database session.
    db.session.add(history)

    # ------------------------------------------------------
    # Create a notification.
    #
    # In Phase 10 this notification will be
    # displayed to supervisors and can later
    # trigger Email and SMS notifications.
    # ------------------------------------------------------

    notification = Notification(

        title="SLA Escalation",

        message=(

            f"Request "

            f"{request.reference_number} "

            f"has exceeded its SLA."

        ),

        notification_type="SYSTEM"

    )
    # Add notification to the database session.
    db.session.add(notification)

    # ------------------------------------------------------
    # Save the history record and notification.
    # ------------------------------------------------------

    db.session.commit()

    # ------------------------------------------------------
    # Escalation completed successfully.
    # ------------------------------------------------------

    return True


# ==========================================================
# Process Multiple Requests
# ==========================================================

def process_all_requests(requests):
    """
    Processes every active request in the system.

    Parameters
    ----------
    requests : list
        List of ServiceRequest objects.

    Returns
    -------
    int
        Number of requests successfully escalated.
    """

    # Counter for successful escalations.
    escalated_count = 0

    # Loop through every request.
    for request in requests:

        # Attempt escalation.
        success = escalate_request(request)

        # Increase counter if successful.
        if success:

            escalated_count += 1

    # Return the total number of escalated requests.
    return escalated_count