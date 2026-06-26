from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from extensions import db

from app.models.request import (
    CitizenRequest
)

from app.services.reference_generator import (
    generate_reference_number
)

from app.integrations.webhook_service import (
    send_request_to_ps_srms
)

request_bp = Blueprint(
    "requests",
    __name__
)


@request_bp.route(
    "/submit-request",
    methods=["POST"]
)
@jwt_required()
def submit_request():
    """
    Citizen submits service request.
    """

    citizen_id = get_jwt_identity()

    data = request.get_json()

    # Generate unique reference.
    reference_number = (
        generate_reference_number()
    )

    # Create local request record.
    citizen_request = CitizenRequest(
        reference_number=reference_number,
        title=data["title"],
        description=data["description"],
        citizen_id=citizen_id
    )

    db.session.add(
        citizen_request
    )

    db.session.commit()
    payload = {

        "reference_number":
        reference_number,

        "citizen_id":
        citizen_id,

        "title":
        data["title"],

        "description":
        data["description"]
    }
    success = send_request_to_ps_srms(
        payload
    )
    if success:

        citizen_request.sync_status = (
            "SENT"
        )

    else:

        citizen_request.sync_status = (
            "FAILED"
        )

    db.session.commit()

    return jsonify(
        {
            "reference_number":
            reference_number,

            "sync_status":
            citizen_request.sync_status
        }
    )