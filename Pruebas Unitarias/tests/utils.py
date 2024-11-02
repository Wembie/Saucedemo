import xml.etree.ElementTree as ET
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def xml_to_pdf(xml_file, pdf_file):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    y = height - 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "Test Report")
    y -= 30

    for testsuite in root.findall("testsuite"):
        suite_name = testsuite.get("name")
        total_tests = testsuite.get("tests")
        failures = testsuite.get("failures")
        errors = testsuite.get("errors")
        skipped = testsuite.get("skipped")

        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, y, f"Suite: {suite_name}")
        y -= 15
        c.setFont("Helvetica", 12)
        c.drawString(
            40,
            y,
            f"Total Tests: {total_tests}, Failures: {failures}, Errors: {errors}, Skipped: {skipped}",
        )
        y -= 20

        for testcase in testsuite.findall("testcase"):
            test_name = testcase.get("name")
            test_time = testcase.get("time")
            status = "Passed"
            system_err = testcase.find("system-err")
            if system_err is not None:
                status = "Failed"

            c.drawString(
                40, y, f"Test: {test_name}, Time: {test_time}s, Status: {status}"
            )
            y -= 15

            if status == "Failed":
                c.setFont("Helvetica-Oblique", 10)
                error_message = (
                    system_err.text.strip() if system_err.text else "No details"
                )
                c.drawString(40, y, f"Error: {error_message}")
                y -= 20
                c.setFont("Helvetica", 12)

        y -= 10

        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
