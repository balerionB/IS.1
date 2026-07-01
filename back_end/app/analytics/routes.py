from flask import Blueprint, send_file
from flask import jsonify

from flask import Blueprint, render_template
from flask_login import login_required

from back_end.app.auth.decorators import role_required
from back_end.app.services.analytics_services import AnalyticsService
from back_end.app.utils.excel_generator import ExcelGenerator
from back_end.app.utils.permissions import roles_required
from back_end.app.utils.report_generator import ReportGenerator

analytics = Blueprint(
    "analytics",
    __name__
)
from flask import jsonify

from back_end.app.services import analytics_services
@analytics.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "analytics/dashboard.html"
    )

analytics_bp = Blueprint(
    "analytics",
    __name__
)

@analytics.route("/api/summary")
@login_required
def summary():

    return jsonify(

        AnalyticsService.get_summary()

    )
@analytics_bp.route(
    "/dashboard"
)
@role_required(
    "SUPERVISOR",
    "OVERSIGHT"
)
def dashboard():

    return jsonify(
        {
            "message":
            "Analytics Dashboard"
        }
    )
@analytics.route("/api/monthly")
@login_required
def monthly():

    return jsonify(

        AnalyticsService.get_monthly_requests()

    )
@analytics.route("/api/departments")
@login_required
def departments():

    return jsonify(

        AnalyticsService.department_performance()

    )


@analytics.route("/api/categories")
@login_required
def categories():

    return jsonify(

        AnalyticsService.category_breakdown()

    )


@analytics.route("/api/sla")
@login_required
def sla():

    return jsonify(

        AnalyticsService.sla_compliance()

    )


@analytics.route("/api/officers")
@login_required
def officers():

    return jsonify(

        AnalyticsService.officer_productivity()

    )
@analytics.route("/reports")
@login_required
def reports():

    return render_template(

        "analytics/reports.html"

    )
@analytics.route("/reports")
@login_required
def reports():

    return render_template(

        "analytics/reports.html"

    )
@analytics.route("/export/pdf")

@login_required

def export_pdf():

    summary = AnalyticsService.generate_report()["summary"]

    filename = ReportGenerator.create_summary_pdf(summary)

    return send_file(

        filename,

        as_attachment=True

    )
@analytics.route("/export/excel")

@login_required

def export_excel():

    summary=AnalyticsService.generate_report()["summary"]

    filename=ExcelGenerator.create(summary)

    return send_file(

        filename,

        as_attachment=True

    )
@analytics.route("/api/insights")

@login_required

def insights():

    return jsonify(

        AnalyticsService.executive_insights()

    )
@analytics.route("/reports")
@login_required
@roles_required(
    "Supervisor",
    "Administrator"
)
def reports():

    ...
