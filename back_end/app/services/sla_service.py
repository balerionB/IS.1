"""
==========================================================
File: sla_service.py

Purpose:
Contains all business logic responsible for
calculating Service Level Agreements (SLAs).

This service DOES NOT modify the database.

It only determines:

1. Remaining SLA time
2. Overdue requests
3. Escalation decisions

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Import datetime utilities.
# ==========================================================

from datetime import datetime
from datetime import timedelta


# ==========================================================
# Default SLA Duration
# ==========================================================

# Every request is expected to be resolved
# within seven (7) days.

DEFAULT_SLA_DAYS = 7


# ==========================================================
# Calculate SLA Deadline
# ==========================================================

def calculate_due_date(created_at):
    """
    Calculates the SLA deadline.

    Parameters
    ----------
    created_at : datetime

    Returns
    -------
    datetime
        The date the request is expected
        to be completed.
    """

    return created_at + timedelta(days=DEFAULT_SLA_DAYS)


# ==========================================================
# Calculate Remaining Time
# ==========================================================

def get_remaining_time(created_at):
    """
    Calculates how much time remains
    before the SLA expires.

    Parameters
    ----------
    created_at : datetime

    Returns
    -------
    timedelta
    """

    due_date = calculate_due_date(created_at)

    return due_date - datetime.utcnow()


# ==========================================================
# Determine Whether SLA Has Been Breached
# ==========================================================

def is_sla_breached(created_at):
    """
    Determines whether a request has
    exceeded its SLA.

    Returns
    -------
    bool
    """

    remaining_time = get_remaining_time(created_at)

    return remaining_time.total_seconds() <= 0


# ==========================================================
# Determine SLA Priority
# ==========================================================

def get_sla_priority(created_at):
    """
    Determines the urgency of a request.

    Returns
    -------
    str
    """

    remaining = get_remaining_time(created_at)

    hours_remaining = remaining.total_seconds() / 3600

    # SLA already exceeded.
    if hours_remaining <= 0:

        return "OVERDUE"

    # Less than one day remaining.
    if hours_remaining <= 24:

        return "CRITICAL"

    # Less than three days remaining.
    if hours_remaining <= 72:

        return "WARNING"

    # Everything is healthy.
    return "NORMAL"