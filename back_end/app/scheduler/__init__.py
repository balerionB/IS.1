"""
==========================================================
File: __init__.py

Purpose:
Initializes the scheduler package.

This file exposes the scheduler object and
helper functions so they can be imported
from other parts of the application.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Import Scheduler
# ==========================================================

# Background APScheduler instance.
from .scheduler import scheduler

# Function that starts the scheduler.
from .scheduler import start_scheduler

# ==========================================================
# Import Job Registration Function
# ==========================================================

# Registers all scheduled background jobs.
from .jobs import register_jobs