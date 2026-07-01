# ==========================================================
# SQLAlchemy
# ==========================================================

from sqlalchemy import func

# Database instance.
from app.extensions import db

# ==========================================================
# Models
# ==========================================================

from app.models.service_request import ServiceRequest

# ==========================================================
# Dashboard Service
# ==========================================================

class DashboardService:
    """
    Calculates statistics
    displayed on the
    analytics dashboard.
    """

    # ======================================================
    # Total Requests
    # ======================================================

    def total_requests(self):
        """
        Returns the total number
        of service requests
        stored in the database.
        """

        # Query the ServiceRequest table
        # and count every record.
        return ServiceRequest.query.count()

    # ======================================================
    # Approved Requests
    # ======================================================

    def approved_requests(self):
        """
        Returns the total number
        of approved service requests.
        """

        # Count every request whose
        # status is APPROVED.
        return ServiceRequest.query.filter_by(

            status="APPROVED"

        ).count()

    # ======================================================
    # Pending Requests
    # ======================================================

    def pending_requests(self):
        """
        Returns the total number
        of pending service requests.

        Pending requests include:
        - SUBMITTED
        - ASSIGNED
        - IN_PROGRESS
        """

        # Count every request whose
        # status is still active.
        return ServiceRequest.query.filter(

            ServiceRequest.status.in_(

                [

                    "SUBMITTED",

                    "ASSIGNED",

                    "IN_PROGRESS"

                ]

            )

        ).count()

    # ======================================================
    # Rejected Requests
    # ======================================================

    def rejected_requests(self):
        """
        Returns the total number
        of rejected service requests.
        """

        # Count every rejected request.
        return ServiceRequest.query.filter_by(

            status="REJECTED"

        ).count()

    # ======================================================
    # Escalated Requests
    # ======================================================

    def escalated_requests(self):
        """
        Returns the total number
        of escalated service requests.
        """

        # Count every request that
        # has exceeded its SLA.
        return ServiceRequest.query.filter_by(

            status="ESCALATED"

        ).count()

    # ======================================================
    # Monthly Request Trends
    # ======================================================

    def monthly_request_trends(self):
        """
        Returns the number of
        service requests grouped
        by month.
        """

        # Query the database and group
        # requests according to the month
        # they were submitted.
        results = db.session.query(

            func.extract(

                "month",

                ServiceRequest.submitted_at

            ).label("month"),

            func.count(

                ServiceRequest.id

            ).label("total")

        ).group_by(

            func.extract(

                "month",

                ServiceRequest.submitted_at

            )

        ).order_by(

            func.extract(

                "month",

                ServiceRequest.submitted_at

            )

        ).all()

        # Convert query results into
        # a JSON-friendly list.
        return [

            {

                "month": int(result.month),

                "total_requests": result.total

            }

            for result in results

        ]

    # ======================================================
    # SLA Compliance
    # ======================================================

    def sla_compliance(self):
        """
        Calculates the percentage
        of requests completed
        without escalation.
        """

        # Get the total number of requests.
        total = self.total_requests()

        # Avoid division by zero.
        if total == 0:

            return 100

        # Get escalated requests.
        escalated = self.escalated_requests()

        # Calculate compliance percentage.
        compliance = (

            (total - escalated)

            / total

        ) * 100

        return round(

            compliance,

            2

        )

    # ======================================================
    # Approval Rate
    # ======================================================

    def approval_rate(self):
        """
        Calculates the percentage
        of approved requests.
        """

        # Get total requests.
        total = self.total_requests()

        if total == 0:

            return 0

        # Get approved requests.
        approved = self.approved_requests()

        # Calculate approval percentage.
        rate = (

            approved

            / total

        ) * 100

        return round(

            rate,

            2

        )

    # ======================================================
    # Escalation Rate
    # ======================================================

    def escalation_rate(self):
        """
        Calculates the percentage
        of escalated requests.
        """

        # Get total requests.
        total = self.total_requests()

        if total == 0:

            return 0

        # Get escalated requests.
        escalated = self.escalated_requests()

        # Calculate escalation percentage.
        rate = (

            escalated

            / total

        ) * 100

        return round(

            rate,

            2

        )