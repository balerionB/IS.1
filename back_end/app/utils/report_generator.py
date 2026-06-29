from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)

from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


class ReportGenerator:

    @staticmethod
    def create_summary_pdf(summary):

        filename = "analytics_report.pdf"

        document = SimpleDocTemplate(filename)

        elements = []

        elements.append(

            Paragraph(
                "County Analytics Report",
                styles["Heading1"]
            )

        )

        table_data = [

            ["Metric","Value"],

            ["Total Requests",summary["total"]],

            ["Resolved",summary["resolved"]],

            ["Pending",summary["pending"]],

            ["SLA",summary["sla"]]

        ]

        table = Table(table_data)

        table.setStyle(

            TableStyle([

                ("GRID",(0,0),(-1,-1),1,colors.black),

                ("BACKGROUND",(0,0),(-1,0),colors.grey),

                ("TEXTCOLOR",(0,0),(-1,0),colors.white),

                ("ALIGN",(0,0),(-1,-1),"CENTER")

            ])

        )

        elements.append(table)

        document.build(elements)

        return filename