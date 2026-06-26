# Environment variables.
import os

# HTTP requests.
import requests

# Load .env variables.
from dotenv import load_dotenv

load_dotenv()


def send_request_to_ps_srms(payload):
    """
    Sends citizen request
    to PS-SRMS.
    """

    # Retrieve webhook URL.
    url = os.getenv(
        "PS_SRMS_WEBHOOK_URL"
    )

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=10
        )

        # Success.
        if response.status_code == 200:

            return True

        return False

    except Exception as error:

        print(
            f"Webhook error: {error}"
        )

        return False