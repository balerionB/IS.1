# Flask imports.
from unittest import result

import form
from flask import Blueprint
from flask import request
from flask import jsonify

# Authentication service.
import app.auth.services

import app.models
import app.requests.routes

import app.models

from app.models import user

import werkzeug.security  # Best practice: imports usually go at the top

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
                    "token": result["token"]
                }
            )
    return jsonify(
        {
            "message":
            "Invalid credentials"
        }
    ), 401




# ... other code ...

def register():
    # All lines below must be indented
    user.password = werkzeug.security.generate_password_hash(
        form.password.data
    )
    # Add a return statement or further logic here if needed   