import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from logging import Logger, basicConfig, INFO

basicConfig(level=INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = Logger("SauceDemoLogger")


class BaseTest(unittest.TestCase):
    screenshots_dir = "screenshots"

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(cls.screenshots_dir):
            os.makedirs(cls.screenshots_dir)
            logger.info(f"Screenshot directory '{cls.screenshots_dir}' created.")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

        self.class_name = self.__class__.__name__.lower()
        self.screenshot_dir = os.path.join(self.screenshots_dir, self.class_name)
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
            logger.info(
                f"Screenshot directory '{self.screenshot_dir}' created for {self.class_name}."
            )

    def tearDown(self):
        self.driver.quit()
