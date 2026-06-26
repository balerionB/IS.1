"""
webhook_service.py

Sends request updates
to PS-SRMS.
"""

import os

import requests

from dotenv import load_dotenv

load_dotenv()


def send_status_update(payload):
    """
    Sends request status update
    to PS-SRMS.
    """

    callback_url = os.getenv(
        "PS_SRMS_CALLBACK"
    )

    try:

        response = requests.post(
            callback_url,
            json=payload,
            timeout=10
        )

        return response.status_code == 200

    except Exception as error:

        print(
            f"Webhook failed: {error}"
        )

        return False