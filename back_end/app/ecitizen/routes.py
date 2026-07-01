"""
==========================================================
File: routes.py

Purpose:
Simulates the Kenyan eCitizen API.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Flask Imports
# ==========================================================

from flask import (

    Blueprint,

    jsonify,

    request

)

# ==========================================================
# Blueprint
# ==========================================================

ecitizen_bp = Blueprint(

    "ecitizen",

    __name__

)

# ==========================================================
# Mock Citizen Database
# ==========================================================

# This simulates records that would
# normally exist inside the real
# eCitizen platform.

MOCK_CITIZENS = [

    {

        "national_id": "12345678",

        "first_name": "Arnold",

        "last_name": "Abonyo",

        "email": "arnold@email.com",

        "phone": "0712345678"

    },

    {

        "national_id": "87654321",

        "first_name": "Grace",

        "last_name": "Achieng",

        "email": "grace@email.com",

        "phone": "0798765432"

    }

]

# ==========================================================
# Citizen Authentication
# ==========================================================

@ecitizen_bp.route(

    "/authenticate",

    methods=["POST"]

)

def authenticate_citizen():
    """
    Simulates citizen authentication.
    """

    # Read JSON request.
    data = request.get_json()

    national_id = data.get(

        "national_id"

    )

    # Search mock database.
    for citizen in MOCK_CITIZENS:

        if citizen["national_id"] == national_id:

            return jsonify({

                "success": True,

                "citizen": citizen

            }), 200

    # Citizen not found.
    return jsonify({

        "success": False,

        "message": "Citizen not found."

    }), 404

# ==========================================================
# Citizen Lookup
# ==========================================================

@ecitizen_bp.route(

    "/citizen/<national_id>",

    methods=["GET"]

)

def get_citizen(national_id):
    ...
