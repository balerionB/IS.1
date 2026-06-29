from openpyxl import Workbook

class ExcelGenerator:

    @staticmethod

    def create(summary):

        workbook=Workbook()

        sheet=workbook.active

        sheet.title="Analytics"

        sheet.append(["Metric","Value"])

        sheet.append(["Total Requests",summary["total"]])

        sheet.append(["Resolved",summary["resolved"]])

        sheet.append(["Pending",summary["pending"]])

        sheet.append(["SLA",summary["sla"]])

        filename="analytics.xlsx"

        workbook.save(filename)

        return filename