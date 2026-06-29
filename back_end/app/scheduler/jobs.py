"""
==========================================================
File: jobs.py

Purpose:
Contains every scheduled background task
used by the PS-SRMS.

Responsibilities:
1. Register scheduled jobs.
2. Monitor SLA deadlines.
3. Process overdue requests.
4. Log scheduler activity.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Scheduler Instance
# ==========================================================

# Import the global scheduler object.
from app.scheduler.scheduler import scheduler

# ==========================================================
# Database Models
# ==========================================================

# Main request model.
from app.models.service_request import ServiceRequest

# ==========================================================
# Escalation Service
# ==========================================================

# Processes overdue requests.
from app.services.escalation_service import (
    process_all_requests
)

# ==========================================================
# Scheduler Logger
# ==========================================================

# Logs scheduler activity with timestamps.
from app.utils.logger import log_scheduler


# ==========================================================
# Register Background Jobs
# ==========================================================

def register_jobs():
    """
    Registers all scheduled background jobs.

    This function is called once when the
    Flask application starts.
    """

    # ------------------------------------------------------
    # Register the SLA Monitoring Job.
    # ------------------------------------------------------

    scheduler.add_job(

        # Function executed by APScheduler.
        func=run_sla_monitor,

        # Execute repeatedly.
        trigger="interval",

        # Run every 5 minutes.
        minutes=5,

        # Unique identifier.
        id="sla_monitor",

        # Prevent duplicate jobs.
        replace_existing=True

    )

    # Log successful registration.
    log_scheduler(
        "SLA Monitoring Job Registered Successfully."
    )


# ==========================================================
# SLA Monitoring Job
# ==========================================================

def run_sla_monitor():
    """
    Executes automatically every five minutes.

    Responsibilities:
    -----------------
    1. Retrieve all active requests.
    2. Check for SLA violations.
    3. Escalate overdue requests.
    4. Display scheduler statistics.
    """

    # ------------------------------------------------------
    # Scheduler starting message.
    # ------------------------------------------------------

    log_scheduler(
        "Starting SLA Monitoring Job..."
    )

    # ------------------------------------------------------
    # Retrieve active requests.
    #
    # Only requests that are still being worked on
    # require SLA monitoring.
    # ------------------------------------------------------

    active_requests = ServiceRequest.query.filter(

        ServiceRequest.status.in_(

            [
                "SUBMITTED",
                "ASSIGNED",
                "IN_PROGRESS"
            ]

        )

    ).all()

    # ------------------------------------------------------
    # Process every active request.
    # ------------------------------------------------------

    escalated = process_all_requests(
        active_requests
    )

    # ------------------------------------------------------
    # Display monitoring statistics.
    # ------------------------------------------------------

    log_scheduler(
        f"Active Requests : {len(active_requests)}"
    )

    log_scheduler(
        f"Escalated Requests : {escalated}"
    )

    # ------------------------------------------------------
    # Job completed successfully.
    # ------------------------------------------------------

    log_scheduler(
        "SLA Monitoring Job Completed Successfully."
    )