from back_end.app.extensions import db
from datetime import datetime

from flask import jsonify, render_template
from flask_jwt_extended import current_user
from flask_login import login_required

from back_end.app.models.user import notifications


class Notification(db.Model):

    __tablename__ = "notifications"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    message = db.Column(
        db.Text,
        nullable=False
    )

    notification_type = db.Column(
        db.String(50)
    )

    is_read = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user = db.relationship(
        "User",
        back_populates="notifications"
    )
    from flask import Blueprint, jsonify
    from flask_login import login_required, current_user

    from back_end.app.models.notification import Notification

    notifications = Blueprint(

        "notifications",

        __name__

    )

    @notifications.route("/api/list")
    @login_required
    def notification_list(self):
        data = Notification.query.filter_by(

            user_id=current_user.id

        ).order_by(

            Notification.created_at.desc()

        ).all()

        return jsonify([

            {

                "id": n.id,

                "title": n.title,

                "message": n.message,

                "is_read": n.is_read,

                "created_at": n.created_at.strftime("%Y-%m-%d %H:%M")

            }

            for n in data

        ])

    @notifications.route("/")
    @login_required
    def notification_page(self):
        return render_template(

            "notifications/notifications.html"

        )


@notifications.route("/api/<int:id>/read", methods=["POST"])
@login_required
def mark_read(id):

    notification = Notification.query.get_or_404(id)

    notification.is_read = True

    db.session.commit()

    return jsonify({"success": True})
@notifications.route("/api/read-all", methods=["POST"])
@login_required
def read_all():

    Notification.query.filter_by(
        user_id=current_user.id,
        is_read=False
    ).update({"is_read": True})

    db.session.commit()

    return jsonify({"success": True})
@notifications.route("/api/<int:id>", methods=["DELETE"])
@login_required
def delete_notification(id):

    notification = Notification.query.get_or_404(id)

    db.session.delete(notification)

    db.session.commit()

    return jsonify({"success": True})

