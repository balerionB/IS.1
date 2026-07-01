"""
==========================================================
File: routes.py

Purpose:
Simulates the County Office System API.

This API allows PS-SRMS to communicate
with a County Office.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Flask Imports
# ==========================================================

from flask import Blueprint
from flask import jsonify
from flask import request

# ==========================================================
# Standard Library
# ==========================================================

# Used to record approval and rejection timestamps.
from datetime import datetime

# ==========================================================
# Blueprint
# ==========================================================

county_bp = Blueprint(
    "county",
    __name__
)

# ==========================================================
# Mock County Request Database
# ==========================================================

# This list simulates the County Office database.
# Every request received from PS-SRMS is stored here.
COUNTY_REQUESTS = [
    {
        "reference_number": "REQ-001",
        "title": "Broken streetlight",
        "status": "PENDING"
    },
    {
        "reference_number": "REQ-002",
        "title": "Blocked drainage",
        "status": "PENDING"
    }
]

# ==========================================================
# Receive Service Request
# ==========================================================

@county_bp.route(
    "/receive-request",
    methods=["POST"]
)
def receive_request():
    """
    Receives a service request
    from PS-SRMS.
    """

    # Read the JSON data sent by PS-SRMS.
    data = request.get_json()

    # Store the request in the mock database.
    COUNTY_REQUESTS.append(data)

    return jsonify({
        "success": True,
        "message": "Request received successfully.",
        "request": data
    }), 201


# ==========================================================
# View Received Requests
# ==========================================================

@county_bp.route(
    "/requests",
    methods=["GET"]
)
def get_requests():
    """
    Returns every request
    stored by the County Office.
    """

    return jsonify(COUNTY_REQUESTS), 200


# ==========================================================
# Approve Service Request
# ==========================================================

@county_bp.route(
    "/approve/<reference_number>",
    methods=["PUT"]
)
def approve_request(reference_number):
    """
    Approves a request received
    by the County Office.
    """

    # Search the County request database.
    for county_request in COUNTY_REQUESTS:

        if county_request["reference_number"] == reference_number:

            # Update the request status.
            county_request["status"] = "APPROVED"

            # Record the approval time.
            county_request["decision_date"] = (
                datetime.utcnow().isoformat()
            )

            return jsonify({

                "success": True,

                "message": "Request approved successfully.",

                "request": county_request

            }), 200

    # Request not found.
    return jsonify({

        "success": False,

        "message": "Request not found."

    }), 404


# ==========================================================
# Reject Service Request
# ==========================================================

@county_bp.route(
    "/reject/<reference_number>",
    methods=["PUT"]
)
def reject_request(reference_number):
    """
    Rejects a County request.

    A rejection reason can
    be supplied in the JSON body.
    """

    # Read the JSON body.
    data = request.get_json()

    # Retrieve the rejection reason.
    reason = data.get(
        "reason",
        "No reason provided."
    )

    # Search the County request database.
    for county_request in COUNTY_REQUESTS:

        if county_request["reference_number"] == reference_number:

            # Update the request status.
            county_request["status"] = "REJECTED"

            # Save the rejection reason.
            county_request["reason"] = reason

            # Record the rejection time.
            county_request["decision_date"] = (
                datetime.utcnow().isoformat()
            )

            return jsonify({

                "success": True,

                "message": "Request rejected successfully.",

                "request": county_request

            }), 200

    # Request not found.
    return jsonify({

        "success": False,

        "message": "Request not found."

    }), 404

