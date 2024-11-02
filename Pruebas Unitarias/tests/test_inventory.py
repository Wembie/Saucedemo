from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest, unittest, logger
from selenium.webdriver.support.ui import Select


class InventoryTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.driver.get("https://www.saucedemo.com/")
        self.path = f"{self.screenshots_dir}/{self.__class__.__name__.lower()}"
        self.login()

    def login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def test_inventory_page_elements(self):
        product_elements = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )
        self.assertTrue(len(product_elements) > 0)
        logger.info("Inventory page loaded successfully with products visible.")

    def test_sort_inventory(self):
        filter_select = Select(
            self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        )
        filter_select.select_by_value("lohi")

        prices = [
            float(item.text[1:])
            for item in self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        ]
        self.assertEqual(prices, sorted(prices))
        logger.info("Inventory sorted by price from low to high successfully.")


if __name__ == "__main__":
    unittest.main()
