from back_end.app.models.notification import Notification
from app import db


class NotificationService:

    @staticmethod
    def create_notification(

        user_id,
        title,
        message,
        notification_type="General"

    ):

        notification = Notification(

            user_id=user_id,

            title=title,

            message=message,

            notification_type=notification_type

        )

        db.session.add(notification)

        db.session.commit()

        return notification