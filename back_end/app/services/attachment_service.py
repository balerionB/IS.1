import uuid

from app import db

from back_end.app.models.attachment import Attachment

from back_end.app.utils.s3_service import S3Service


class AttachmentService:

    @staticmethod
    def upload(file, request_id, user_id):

        key = f"{uuid.uuid4()}_{file.filename}"

        S3Service.upload(

            file,

            key

        )

        attachment = Attachment(

            request_id=request_id,

            uploaded_by=user_id,

            file_name=file.filename,

            s3_key=key,

            content_type=file.content_type,

            file_size=file.content_length

        )

        db.session.add(

            attachment

        )

        db.session.commit()

        return attachment

    @staticmethod
    def delete(attachment):
        S3Service.delete(

            attachment.s3_key

        )

        db.session.delete(

            attachment

        )

        db.session.commit()