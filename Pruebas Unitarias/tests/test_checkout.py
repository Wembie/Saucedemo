from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest, unittest, logger


class CheckoutTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.driver.get("https://www.saucedemo.com/")
        self.login()

    def login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    def test_checkout_process(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()

        self.driver.find_element(By.ID, "first-name").send_keys("Juan")
        self.driver.find_element(By.ID, "last-name").send_keys("Acosta")
        self.driver.find_element(By.ID, "postal-code").send_keys("123987")
        self.driver.find_element(By.ID, "continue").click()

        overview_title = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        self.assertEqual(overview_title.text, "Checkout: Overview")
        logger.info(
            "Checkout information entered successfully and overview page displayed."
        )

        self.driver.find_element(By.ID, "finish").click()
        complete_message = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        self.assertEqual(complete_message.text, "Thank you for your order!")
        logger.info("Order completed successfully.")


if __name__ == "__main__":
    unittest.main()
