from app import create_app

from app.extensions import db

from app.models.user import User

app = create_app()

with app.app_context():

    supervisor = User(
        name="System Supervisor",
        email="supervisor@pssrms.com",
        role="SUPERVISOR"
    )

    supervisor.set_password(
        "Admin123!"
    )

    db.session.add(
        supervisor
    )

    db.session.commit()

    print(
        "Supervisor created."
    )