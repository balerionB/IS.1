# Import JWT token generator.
from flask_jwt_extended import create_access_token

# Import user model.
from app.models.user import User


def authenticate_user(email, password):
    """
    Validates credentials and
    generates JWT token.
    """

    user = User.query.filter_by(
        email=email
    ).first()

    # User not found.
    if not user:
        return None

    # Wrong password.
    if not user.check_password(password):
        return None

    # Generate JWT token.

    token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "role": user.role
        }
    )

    return {
        "user": user,
        "token": token
    }