from base_test import BaseTest, unittest


class InventoryTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.path = f"{self.screenshots_dir}/{self.__class__.__name__.lower()}"

    def test_inventory_page(self):
        pass


if __name__ == "__main__":
    unittest.main()
