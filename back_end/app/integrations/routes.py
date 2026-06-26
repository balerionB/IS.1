from flask import Blueprint
from flask import jsonify
from flask import request

from extensions import db

from app.models.service_request import (
    ServiceRequest
)

from datetime import datetime
from datetime import timedelta

integration_bp = Blueprint(
    "integrations",
    __name__
)
@integration_bp.route(
    "/ecitizen/request",
    methods=["POST"]
)
def receive_ecitizen_request():
    """
    Receives citizen requests
    from eCitizen.
    """
    data = request.get_json()


required_fields = [
    "reference_number",
    "title"
]

for field in required_fields:

    if field not in data:
        return jsonify(
            {
                "message":
                    f"{field} missing"
            }
        ), 400
    request_record = ServiceRequest(

        reference_number=
        data["reference_number"],

        title=
        data["title"],

        description=
        data.get(
            "description"
        ),

        status="SUBMITTED",

        sla_deadline=
        datetime.utcnow()
        + timedelta(days=7)
    )
    db.session.add(
        request_record
    )

    db.session.commit()
    return jsonify(
        {
            "message":
            "Request received."
        }
    ), 200
@integration_bp.route(
    "/county/status-update",
    methods=["POST"]
)
def receive_county_status_update():
    """
    Receives status updates from the
    County Office System.
    """

    # Read the JSON payload.
    data = request.get_json()

    # Validate required fields.
    required_fields = [
        "reference_number",
        "status"
    ]

    for field in required_fields:

        if field not in data:

            return jsonify({
                "message": f"{field} is required."
            }), 400

    # Find the matching service request.
    request_record = ServiceRequest.query.filter_by(
        reference_number=data["reference_number"]
    ).first()

    if request_record is None:

        return jsonify({
            "message": "Request not found."
        }), 404

    # Store the previous status before updating.
    previous_status = request_record.status

    # Update to the new status.
    request_record.status = data["status"]

    # Save the change.
    db.session.commit()

    # Record the workflow transition.
    status_history = RequestStatusHistory(
        request_id=request_record.id,
        old_status=previous_status,
        new_status=request_record.status,
        changed_by=None,          # External system initiated
        actor_role="COUNTY_SYSTEM",
        reason="Status update received from County Office System"
    )

    db.session.add(status_history)
    db.session.commit()

    return jsonify({
        "message": "Status update processed successfully."
    }), 200