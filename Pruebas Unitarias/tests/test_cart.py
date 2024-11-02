from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest, unittest, logger


class CartTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.driver.get("https://www.saucedemo.com/")
        self.login()

    def login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def test_add_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        cart_badge = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        self.assertEqual(cart_badge.text, "1")
        logger.info("Product added to cart successfully.")

    def test_remove_from_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        cart_badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(len(cart_badge), 0)
        logger.info("Product removed from cart successfully.")


if __name__ == "__main__":
    unittest.main()
