from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_test import BaseTest, unittest, os, logger


class LoginTests(BaseTest):
    users = [
        "standard_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user",
        "locked_out_user",  # ERROR Epic sadface: Sorry, this user has been locked out.
    ]
    password = "secret_sauce"

    pages_to_test = {
        "https://www.saucedemo.com/cart.html": "Epic sadface: You can only access '/cart.html' when you are logged in.",
        "https://www.saucedemo.com/inventory.html": "Epic sadface: You can only access '/inventory.html' when you are logged in.",
        "https://www.saucedemo.com/checkout-step-one.html": "Epic sadface: You can only access '/checkout-step-one.html' when you are logged in.",
        "https://www.saucedemo.com/checkout-step-two.html": "Epic sadface: You can only access '/checkout-step-two.html' when you are logged in.",
        "https://www.saucedemo.com/checkout-complete.html": "Epic sadface: You can only access '/checkout-complete.html' when you are logged in.",
    }

    def setUp(self):
        super().setUp()
        self.driver.get("https://www.saucedemo.com/")
        self.path = f"{self.screenshots_dir}/{self.__class__.__name__.lower()}"

    def test_login(self):
        driver = self.driver

        for user in self.users:
            username_field = self.wait.until(
                EC.visibility_of_element_located((By.ID, "user-name"))
            )
            password_field = driver.find_element(By.ID, "password")
            login_button = driver.find_element(By.ID, "login-button")

            username_field.clear()
            password_field.clear()
            username_field.send_keys(user)
            password_field.send_keys(self.password)
            login_button.click()

            try:
                inventory_title = self.wait.until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "title"))
                )
                self.assertEqual(inventory_title.text, "Products")
                logger.info(f"Login successful for user: {user}")
                self.logout(user)
            except Exception:
                self.handle_login_failure(user)

    def logout(self, user):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        logout_button = self.wait.until(
            EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
        )
        logout_button.click()
        logger.info(f"User {user} logged out successfully.")

    def handle_login_failure(self, user):
        try:
            error_message = self.driver.find_element(
                By.CLASS_NAME, "error-message-container"
            ).text
            logger.warning(f"Login failed for user: {user} with error: {error_message}")
        except Exception:
            logger.warning(
                f"Login failed for user: {user} without visible error message."
            )

        screenshot_path = os.path.join(self.path, f"{user}_login_failure.png")
        self.driver.save_screenshot(screenshot_path)
        logger.error(f"Screenshot for user {user} failure saved at {screenshot_path}")

    def test_access_pages_without_login(self):
        for page, expected_error in self.pages_to_test.items():
            with self.subTest(page=page):
                self.driver.get(page)
                try:
                    error_message = self.wait.until(
                        EC.visibility_of_element_located(
                            (By.CLASS_NAME, "error-message-container")
                        )
                    ).text
                    self.assertEqual(error_message, expected_error)
                    logger.info(
                        f"Access to page '{page}' correctly blocked without login."
                    )
                except Exception as e:
                    logger.error(
                        f"Failed to verify error message for accessing '{page}'."
                    )
                    screenshot_path = os.path.join(
                        self.path,
                        f"access_{page.split('/')[-1]}_without_login_failure.png",
                    )
                    self.driver.save_screenshot(screenshot_path)
                    logger.error(f"Screenshot saved at {screenshot_path}")


if __name__ == "__main__":
    unittest.main()
