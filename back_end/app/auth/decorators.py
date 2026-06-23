from functools import wraps

from flask import jsonify

from flask_jwt_extended import (
    get_jwt,
    verify_jwt_in_request
)


def role_required(*allowed_roles):
    """
    Restricts endpoint access
    to specific roles.
    """

    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):

            verify_jwt_in_request()

            claims = get_jwt()

            role = claims.get("role")

            if role not in allowed_roles:

                return jsonify(
                    {
                        "message":
                        "Access denied"
                    }
                ), 403

            return fn(
                *args,
                **kwargs
            )

        return decorator

    return wrapper