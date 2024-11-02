import unittest
import os
from xmlrunner import XMLTestRunner
from test_login import LoginTests
from test_inventory import InventoryTests
from test_cart import CartTests
from test_checkout import CheckoutTests
from base_test import logger
from utils import xml_to_pdf

os.makedirs("reports", exist_ok=True)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoginTests))
    suite.addTest(unittest.makeSuite(InventoryTests))
    suite.addTest(unittest.makeSuite(CartTests))
    suite.addTest(unittest.makeSuite(CheckoutTests))
    return suite


if __name__ == "__main__":
    xml_path = "reports/test_report.xml"
    pdf_path = "reports/test_report.pdf"

    with open(xml_path, "wb") as output:
        runner = XMLTestRunner(output=output)
        runner.run(suite())

    try:
        xml_to_pdf(xml_path, pdf_path)
        logger.info(f"PDF report generated in {pdf_path}")
    except Exception as e:
        logger.error(f"Error converting XML to PDF: {e}")
