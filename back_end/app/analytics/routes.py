from flask import Blueprint
from flask import jsonify

from app.auth.decorators import (
    role_required
)

analytics_bp = Blueprint(
    "analytics",
    __name__
)


@analytics_bp.route(
    "/dashboard"
)
@role_required(
    "SUPERVISOR",
    "OVERSIGHT"
)
def dashboard():

    return jsonify(
        {
            "message":
            "Analytics Dashboard"
        }
    )