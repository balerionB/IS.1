from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request

from app.extensions import db
from app.models.request_status_history import RequestStatusHistory
from app.models.service_request import ServiceRequest
from app.services.synchronization_service import SynchronizationService

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
    data = request.get_json() or {}

    required_fields = [
        "reference_number",
        "title"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify(
                {
                    "message": f"{field} missing"
                }
            ), 400

    request_record = ServiceRequest(
        reference_number=data["reference_number"],
        title=data["title"],
        description=data.get("description"),
        status="SUBMITTED",
        sla_deadline=datetime.utcnow() + timedelta(days=7)
    )

    db.session.add(request_record)
    db.session.commit()

    return jsonify(
        {
            "message": "Request received."
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
    data = request.get_json() or {}

    required_fields = [
        "reference_number",
        "status"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify(
                {
                    "message": f"{field} is required."
                }
            ), 400

    request_record = ServiceRequest.query.filter_by(
        reference_number=data["reference_number"]
    ).first()

    if request_record is None:
        return jsonify(
            {
                "message": "Request not found."
            }
        ), 404

    previous_status = request_record.status
    request_record.status = data["status"]
    db.session.commit()

    status_history = RequestStatusHistory(
        request_id=request_record.id,
        old_status=previous_status,
        new_status=request_record.status,
        changed_by=None,
        actor_role="COUNTY_SYSTEM",
        reason="Status update received from County Office System"
    )

    db.session.add(status_history)
    db.session.commit()

    return jsonify(
        {
            "message": "Status update processed successfully."
        }
    ), 200


@integration_bp.route(
    "/authenticate-citizen",
    methods=["POST"]
)
def authenticate_citizen():
    """
    Authenticates a citizen
    through the simulated
    eCitizen API.
    """
    data = request.get_json() or {}
    national_id = data.get("national_id")

    sync_service = SynchronizationService()
    response = sync_service.authenticate_citizen(national_id)

    return jsonify(response)


@integration_bp.route(
    "/send-request",
    methods=["POST"]
)
def send_request():
    """
    Sends a PS-SRMS request
    to the County Office.
    """
    request_data = request.get_json() or {}

    sync_service = SynchronizationService()
    response = sync_service.send_request_to_county(request_data)

    return jsonify(response)


@integration_bp.route(
    "/county-requests",
    methods=["GET"]
)
def county_requests():
    """
    Retrieves every request
    stored by the County Office.
    """
    sync_service = SynchronizationService()
    response = sync_service.get_county_requests()

    return jsonify(response)
