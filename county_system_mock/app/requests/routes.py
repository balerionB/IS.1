"""
Request management routes.
"""

from flask import Blueprint
from flask import jsonify

from flask_jwt_extended import jwt_required

from app.models.request import CountyRequest

from app.integrations.webhook_service import (
    send_status_update
)

from flask_jwt_extended import get_jwt_identity
request_bp = Blueprint(
    "requests",
    __name__
)
@request_bp.route(
    "/queue",
    methods=["GET"]
)
@jwt_required()
def request_queue():
    """
    Returns all pending requests.
    """

    requests = CountyRequest.query.filter_by(
        status="SUBMITTED"
    ).all()

    results = []

    for item in requests:

        results.append({

            "reference_number":
                item.reference_number,

            "title":
                item.title,

            "status":
                item.status

        })

    return jsonify(results)
@request_bp.route(
    "/assign/<int:request_id>",
    methods=["PUT"]
)
@jwt_required()
def assign_request(request_id):
    """
    Assign a request to a county officer.

    URL Example:
    PUT /api/requests/assign/5
    """

    # Retrieve JSON sent by the client
    data = request.get_json()

    # Find the request
    county_request = CountyRequest.query.get(request_id)

    if county_request is None:

        return jsonify({
            "message": "Request not found."
        }), 404

    # Assign officer
    county_request.assigned_to = data["manager_id"]

    # Change workflow state
    county_request.status = "ASSIGNED"

    # Save changes
    db.session.commit()

    return jsonify({
        "message": "Request assigned successfully."
    }), 200

@request_bp.route(
    "/my-requests",
    methods=["GET"]
)
@jwt_required()
def my_requests():
    """
    Return all requests assigned
    to the currently logged-in manager.
    """

    # Extract manager ID from JWT
    manager_id = get_jwt_identity()

    # Retrieve assigned requests
    requests = CountyRequest.query.filter_by(
        assigned_to=manager_id
    ).all()

    response = []

    for item in requests:

        response.append({

            "reference_number":
                item.reference_number,

            "title":
                item.title,

            "status":
                item.status

        })

    return jsonify(response)

@request_bp.route(
    "/update-status/<int:request_id>",
    methods=["PUT"]
)
@jwt_required()
def update_status(request_id):
    """
    Update workflow status.
    """

    data = request.get_json()

    county_request = CountyRequest.query.get(request_id)

    if county_request is None:

        return jsonify({
            "message": "Request not found."
        }), 404

    county_request.status = data["status"]

    db.session.commit()

    return jsonify({

        "message":
            "Status updated.",

        "status":
            county_request.status

    })
# Notify PS-SRMS that the request status has changed.

payload = {

    "reference_number":
        county_request.reference_number,

    "status":
        county_request.status

}

success = send_status_update(payload)

# Optional logging.
if not success:

    print(
        "Unable to notify PS-SRMS."
    )
