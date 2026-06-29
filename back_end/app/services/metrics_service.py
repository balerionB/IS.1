"""
==========================================================
File: metrics_service.py

Purpose:
Calculates SLA monitoring statistics
for the dashboard.

Author:
Arnold Abonyo
==========================================================
"""

from app.models.service_request import ServiceRequest


def get_sla_metrics():
    """
    Returns SLA statistics.
    """

    total_requests = ServiceRequest.query.count()

    active_requests = ServiceRequest.query.filter(

        ServiceRequest.status.in_(

            [
                "SUBMITTED",
                "ASSIGNED",
                "IN_PROGRESS"
            ]

        )

    ).count()

    escalated_requests = ServiceRequest.query.filter_by(

        status="ESCALATED"

    ).count()

    resolved_requests = ServiceRequest.query.filter_by(

        status="RESOLVED"

    ).count()

    return {

        "total_requests":
            total_requests,

        "active_requests":
            active_requests,

        "escalated_requests":
            escalated_requests,

        "resolved_requests":
            resolved_requests

    }