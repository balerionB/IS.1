from flask import Blueprint, jsonify
from flask_login import login_required

from app.services.activity_service import ActivityService

requests_bp = Blueprint("requests", __name__)


@requests_bp.route("/<int:id>/timeline")
@login_required
def get_timeline(id):
    """
    Returns the activity history for a specific request.
    """
    return jsonify(
        ActivityService.request_history(id)
    )