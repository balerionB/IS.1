"""
==========================================================
File: integration_service.py

Purpose:
Provides a single service layer for communicating
with external systems such as:

1. eCitizen
2. County Office System

This service hides all communication details
from the rest of the application.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# HTTP Requests
# ==========================================================

# Used to communicate with external REST APIs.
import requests

# ==========================================================
# Configuration
# ==========================================================

from flask import current_app

# ==========================================================
# Integration Service
# ==========================================================

class IntegrationService:
    """
    Centralized communication layer
    for every external system.
    """

    def __init__(self):
        """
        Initializes the service.

        Reads API URLs from
        the application configuration.
        """

        # --------------------------------------------------
        # eCitizen API Base URL
        # --------------------------------------------------
        # This URL is used whenever the system
        # communicates with the simulated
        # eCitizen service.
        self.ecitizen_url = current_app.config.get(
            "ECITIZEN_API_URL"
        )

        # --------------------------------------------------
        # County Office API Base URL
        # --------------------------------------------------
        # This URL is used whenever the system
        # communicates with the simulated
        # County Office System.
        self.county_url = current_app.config.get(
            "COUNTY_API_URL"
        )

    # ======================================================
    # Health Check
    # ======================================================

    def check_connection(self, url):
        """
        Checks whether an external
        service is reachable.

        Parameters
        ----------
        url : str
            API endpoint to test.

        Returns
        -------
        bool
            True if the service responds
            successfully, otherwise False.
        """

        try:

            # ----------------------------------------------
            # Send a simple GET request to the API.
            # ----------------------------------------------
            response = requests.get(

                url,

                # Wait at most 5 seconds before timing out.
                timeout=5

            )

            # ----------------------------------------------
            # A status code of 200 means the
            # service is reachable.
            # ----------------------------------------------
            return response.status_code == 200

        except Exception as error:

            # ----------------------------------------------
            # If any error occurs (timeout, server offline,
            # connection refused, etc.), return False.
            # ----------------------------------------------
            print(f"Connection Error: {error}")

            return False