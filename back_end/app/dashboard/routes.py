"""
==========================================================
File: routes.py

Purpose:
Provides analytics endpoints
for the PS-SRMS dashboard.

Author:
Arnold Abonyo
==========================================================
"""

# ==========================================================
# Flask Imports
# ==========================================================

from flask import (
    Blueprint,
    jsonify
)

# ==========================================================
# Dashboard Service
# ==========================================================

from app.services.dashboard_service import (
    DashboardService
)

# ==========================================================
# Blueprint
# ==========================================================

dashboard_bp = Blueprint(

    "dashboard",

    __name__

)

# ==========================================================
# Service Instance
# ==========================================================

# Create one DashboardService object
# that will be reused by all routes.
dashboard_service = DashboardService()

# ==========================================================
# Dashboard Summary
# ==========================================================

@dashboard_bp.route(

    "/summary",

    methods=["GET"]

)
def dashboard_summary():
    """
    Returns a summary of the
    dashboard statistics.

    This endpoint is mainly used by
    County Managers and Supervisors
    to view overall system performance.
    """

    # ----------------------------------------------
    # Collect every dashboard statistic.
    # ----------------------------------------------

    summary = {

        # Total number of requests.
        "total_requests":
            dashboard_service.total_requests(),

        # Approved requests.
        "approved_requests":
            dashboard_service.approved_requests(),

        # Pending requests.
        "pending_requests":
            dashboard_service.pending_requests(),

        # Rejected requests.
        "rejected_requests":
            dashboard_service.rejected_requests(),

        # Escalated requests.
        "escalated_requests":
            dashboard_service.escalated_requests()

    }

    # ----------------------------------------------
    # Return the statistics as JSON.
    # ----------------------------------------------

    return jsonify(

        summary

    ), 200


# ==========================================================
# Monthly Request Trends
# ==========================================================

@dashboard_bp.route(

    "/trends",

    methods=["GET"]

)
def monthly_trends():
    """
    Returns the monthly request
    statistics.

    This endpoint is consumed by
    the frontend to generate
    Chart.js graphs.
    """

    # ----------------------------------------------
    # Retrieve monthly trend data.
    # ----------------------------------------------

    trends = dashboard_service.monthly_request_trends()

    # ----------------------------------------------
    # Return trend data as JSON.
    # ----------------------------------------------

    return jsonify(

        trends

    ), 200


# ==========================================================
# Dashboard Performance Metrics
# ==========================================================

@dashboard_bp.route(

    "/performance",

    methods=["GET"]

)
def performance_metrics():
    """
    Returns the key performance
    indicators (KPIs) used by
    the analytics dashboard.

    Includes:

    • SLA Compliance
    • Approval Rate
    • Escalation Rate
    """

    # ----------------------------------------------
    # Build performance statistics.
    # ----------------------------------------------

    performance = {

        # Percentage of requests
        # completed within SLA.
        "sla_compliance":

            dashboard_service.sla_compliance(),

        # Percentage of approved requests.
        "approval_rate":

            dashboard_service.approval_rate(),

        # Percentage of escalated requests.
        "escalation_rate":

            dashboard_service.escalation_rate()

    }

    # ----------------------------------------------
    # Return performance metrics.
    # ----------------------------------------------

    return jsonify(

        performance

    ), 200