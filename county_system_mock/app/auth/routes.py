"""
Authentication routes
for County Office System.
"""

from flask import Blueprint
from flask import request
from flask import jsonify

from flask_jwt_extended import create_access_token

from app.models.county_manager import CountyManager

auth_bp = Blueprint(
    "auth",
    __name__
)
@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():
    """
    Authenticates a county manager.
    """

    data = request.get_json()

    manager = CountyManager.query.filter_by(
        email=data["email"]
    ).first()

    if manager is None:

        return jsonify({
            "message": "Manager not found"
        }), 404

    if not manager.check_password(
        data["password"]
    ):

        return jsonify({
            "message": "Invalid password"
        }), 401

    token = create_access_token(
        identity=str(manager.id),
        additional_claims={
            "role": manager.role
        }
    )

    return jsonify({

        "access_token": token,

        "manager": manager.full_name,

        "department": manager.department

    }), 200