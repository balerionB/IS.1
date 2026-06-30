# Flask imports.
from unittest import result

import form
from flask import Blueprint
from flask import request
from flask import jsonify

# Authentication service.
from back_end.app.auth.services import authenticate_user

from back_end.app.models import user
from back_end.app.requests.routes import form

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
    from werkzeug.security import check_password_hash

    if check_password_hash(

            user.password,

            form.password.data

    ):

    if result:
        return jsonify(
            {
                "token":
                    result["token"]
            }
        )

    return jsonify(
        {
            "message":
            "Invalid credentials"
        }
    ), 401


def register():
import werkzeug.security

user.password = werkzeug.security.generate_password_hash(

    form.password.data

)