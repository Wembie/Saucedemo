import unittest
from test_login import LoginTests
from test_inventory import InventoryTests
from test_cart import CartTests
from test_checkout import CheckoutTests


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(LoginTests))
    suite.addTest(unittest.makeSuite(InventoryTests))
    suite.addTest(unittest.makeSuite(CartTests))
    suite.addTest(unittest.makeSuite(CheckoutTests))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
