# ==========================================================
# HTTP Library
# ==========================================================

import requests

# ==========================================================
# Flask Configuration
# ==========================================================

from flask import current_app

# ==========================================================
# Synchronization Service
# ==========================================================

class SynchronizationService:
    """
    Responsible for sending
    and receiving data from
    external systems.
    """

    def __init__(self):
        """
        Initializes the synchronization service.

        Retrieves the base URLs of the
        simulated external systems from
        the Flask application configuration.
        """

        # --------------------------------------------------
        # eCitizen API Base URL
        # --------------------------------------------------
        self.ecitizen_url = current_app.config.get(
            "ECITIZEN_API_URL"
        )

        # --------------------------------------------------
        # County Office API Base URL
        # --------------------------------------------------
        self.county_url = current_app.config.get(
            "COUNTY_API_URL"
        )

    # ======================================================
    # Send Request to County Office
    # ======================================================

    def send_request_to_county(
        self,
        request_data
    ):
        """
        Sends a service request
        from PS-SRMS to the
        simulated County Office.
        """

        try:

            # Send the request data to the County API.
            response = requests.post(

                f"{self.county_url}/receive-request",

                json=request_data,

                # Wait up to 10 seconds.
                timeout=10

            )

            # Return the JSON response.
            return response.json()

        except Exception as error:

            # Return an error message if communication fails.
            return {

                "success": False,

                "message": str(error)

            }

    # ======================================================
    # Authenticate Citizen
    # ======================================================

    def authenticate_citizen(
        self,
        national_id
    ):
        """
        Authenticates a citizen
        using the simulated
        eCitizen API.
        """

        try:

            # Send the National ID to eCitizen.
            response = requests.post(

                f"{self.ecitizen_url}/authenticate",

                json={

                    "national_id": national_id

                },

                timeout=10

            )

            # Return the authentication result.
            return response.json()

        except Exception as error:

            return {

                "success": False,

                "message": str(error)

            }

    # ======================================================
    # Retrieve County Requests
    # ======================================================

    def get_county_requests(self):
        """
        Retrieves every service request
        currently stored by the
        simulated County Office.
        """

        try:

            # Request all stored County requests.
            response = requests.get(

                f"{self.county_url}/requests",

                timeout=10

            )

            # Return the list of requests.
            return response.json()

        except Exception as error:

            return {

                "success": False,

                "message": str(error)

            }
        
        