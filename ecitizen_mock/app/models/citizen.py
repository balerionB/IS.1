from app import db
from flask_login import UserMixin


class Citizen(UserMixin, db.Model):

    __tablename__ = "citizens"

    id = db.Column(db.Integer, primary_key=True)

    national_id = db.Column(db.String(20), unique=True, nullable=False)

    first_name = db.Column(db.String(100), nullable=False)

    last_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    phone_number = db.Column(db.String(20), nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, server_default=db.func.now())