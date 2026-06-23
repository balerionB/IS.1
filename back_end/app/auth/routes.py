# Flask imports.
from flask import Blueprint
from flask import request
from flask import jsonify

# Authentication service.
from app.auth.services import authenticate_user


# Create blueprint.

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
    Login endpoint.
    """

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    result = authenticate_user(
        email,
        password
    )

    if not result:

        return jsonify(
            {
                "message":
                "Invalid credentials"
            }
        ), 401

    return jsonify(
        {
            "token":
            result["token"]
        }
    )