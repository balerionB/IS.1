from flask import Blueprint, request, jsonify, abort
from flask_login import login_required, current_user

from back_end.app.models import Attachment, attachment
from back_end.app.services.attachment_service import AttachmentService
from back_end.app.utils.permissions import roles_required
from back_end.app.utils.s3_service import S3Service

attachments = Blueprint(
    "attachments",
    __name__
)

from flask import redirect
@attachments.route("/download/<int:id>")
@login_required
def download(id):

    attachment = Attachment.query.get_or_404(id)

    if (
        attachment.request.citizen_id != current_user.id
        and not current_user.is_staff
    ):
        abort(403)

    url = S3Service.generate_download_url(
        attachment.s3_key
    )

    return redirect(url)


    return redirect(url)
@attachments.route("/upload/<int:request_id>", methods=["POST"])
@login_required
def upload(request_id):

    uploaded_file = request.files.get("file")

    if not uploaded_file:

        return jsonify(
            {"error": "No file uploaded."}
        ), 400

    attachment = AttachmentService.upload(
        uploaded_file,
        request_id,
        current_user.id
    )

    return jsonify({
        "id": attachment.id,
        "file_name": attachment.file_name
    }), 201

ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "pdf",
    "doc",
    "docx"
}

MAX_SIZE = 10 * 1024 * 1024   # 10 MB

def allowed(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )
@attachments.route("/upload/<int:request_id>", methods=["POST"])
@login_required
def upload(request_id):

    uploaded_file = request.files.get("file")

    if not uploaded_file:

        return jsonify(
            {"error": "No file uploaded."}
        ), 400

    if not allowed(uploaded_file.filename):

        return jsonify(
            {"error": "Unsupported file type."}
        ), 400

    if request.content_length > MAX_SIZE:

        return jsonify(
            {"error": "File too large."}
        ), 400

    attachment = AttachmentService.upload(
        uploaded_file,
        request_id,
        current_user.id
    )

    return jsonify({
        "success": True
    })
@attachments.route("/preview/<int:id>")
@login_required
def preview(id):

    attachment = Attachment.query.get_or_404(id)

    if (
        attachment.request.citizen_id != current_user.id
        and not current_user.is_staff
    ):
        abort(403)

    return redirect(

        S3Service.generate_download_url(

            attachment.s3_key

        )

    )
@attachments.route("/delete/<int:id>", methods=["DELETE"])
@login_required
def delete(id):

    attachment = Attachment.query.get_or_404(id)

    if not (
        current_user.is_admin
        or attachment.uploaded_by == current_user.id
    ):
        abort(403)

    AttachmentService.delete(
        attachment
    )

    return jsonify({
        "success": True
    })
@attachments.route("/delete/<int:id>")
@login_required
@roles_required(
    "Administrator"
)
