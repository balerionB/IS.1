# Timestamp utility.
from datetime import datetime


def generate_reference_number():
    """
    Generates unique request reference.
    """

    timestamp = datetime.utcnow()

    return (
        "REQ-" +
        timestamp.strftime(
            "%Y%m%d%H%M%S"
        )
    )