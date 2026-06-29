"""
==========================================================
File: logger.py

Purpose:
Provides a reusable logging function.

Author:
Arnold Abonyo
==========================================================
"""

from datetime import datetime


def log_scheduler(message):
    """
    Prints scheduler messages with timestamps.
    """

    current_time = datetime.utcnow()

    print(
        f"[{current_time}] {message}"
    )