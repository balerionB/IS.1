from flask import request
from back_end.app.extensions import db
from back_end.app.models.audit_log import AuditLog


class AuditService:

    @staticmethod
    def log(user_id, action, module, description):

        log = AuditLog(
            user_id=user_id,
            action=action,
            module=module,
            description=description,
            ip_address=request.remote_addr
        )

        db.session.add(log)
        db.session.commit()