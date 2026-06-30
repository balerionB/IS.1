from flask_mail import Message
from back_end.app.extensions import mail


class EmailService:

    @staticmethod
    def send(to, subject, body):

        message = Message(
            subject,
            recipients=[to]
        )

        message.body = body

        mail.send(message)