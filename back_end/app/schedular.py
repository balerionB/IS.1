"""
scheduler.py

Creates and configures the application's
background scheduler.

Author: Arnold Abonyo
Project: PS-SRMS
"""

# Import APScheduler.
from apscheduler.schedulers.background import BackgroundScheduler

# Create a global scheduler instance.
#
# This object manages all scheduled jobs.
scheduler = BackgroundScheduler()


def start_scheduler():
    """
    Starts the scheduler if it
    is not already running.
    """

    # Prevent multiple scheduler instances.
    if not scheduler.running:

        scheduler.start()

        print(
            "Background Scheduler Started Successfully."
        )