from flask import Blueprint
from flask import request
from flask import jsonify

from extensions import db

from app.models.citizen import Citizen

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():

    data = request.get_json()

    citizen = Citizen(
        national_id=data["national_id"],
        full_name=data["full_name"],
        email=data["email"],
        phone=data["phone"]
    )

    citizen.set_password(
        data["password"]
    )

    db.session.add(
        citizen
    )

    db.session.commit()

    return jsonify(
        {
            "message":
            "Citizen registered."
        }
    )

from flask_jwt_extended import (
    create_access_token
)
@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()

    citizen = Citizen.query.filter_by(
        email=data["email"]
    ).first()

    if not citizen:

        return jsonify(
            {"message": "Invalid user"}
        ), 401

    if not citizen.check_password(
        data["password"]
    ):

        return jsonify(
            {"message": "Invalid password"}
        ), 401

    token = create_access_token(
        identity=str(citizen.id)
    )

    return jsonify(
        {
            "token": token
        }
    )