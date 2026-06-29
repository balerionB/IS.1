"""
==========================================================
File: scheduler.py

Purpose:
Creates and manages the APScheduler
background scheduler.

Author:
Arnold Abonyo
==========================================================
"""

# Import APScheduler.
from apscheduler.schedulers.background import (
    BackgroundScheduler
)

# Global scheduler instance.
scheduler = BackgroundScheduler()


def start_scheduler():
    """
    Starts APScheduler.
    """

    # Prevent starting twice.
    if not scheduler.running:

        scheduler.start()

        print("=" * 60)
        print("Background Scheduler Started Successfully")
        print("=" * 60)