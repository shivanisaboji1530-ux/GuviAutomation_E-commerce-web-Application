import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from utils.config import USERNAME, PASSWORD


class TestSorting:

    def test_sort_products_name_a_to_z(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        products.sort_products("Name (A to Z)")

        assert products.verify_name_a_to_z()

        page.screenshot(path="screenshots/test_sort_products_name_a_to_z.png")

    def test_sort_products_name_z_to_a(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        products.sort_products("Name (Z to A)")

        assert products.verify_name_z_to_a()

        page.screenshot(path="screenshots/test_sort_products_name_z_to_a.png")

    def test_sort_products_price_low_to_high(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        products.sort_products("Price (low to high)")

        assert products.verify_price_low_to_high()

        page.screenshot(path="screenshots/test_sort_products_price_low_to_high.png")

    def test_sort_products_price_high_to_low(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        products.sort_products("Price (high to low)")

        assert products.verify_price_high_to_low()

        page.screenshot(path="screenshots/test_sort_products_price_high_to_low.png")