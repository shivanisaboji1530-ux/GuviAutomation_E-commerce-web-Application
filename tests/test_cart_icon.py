from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from utils.config import USERNAME, PASSWORD


class TestCartIcon:

    def test_cart_icon_visibility(self, page):
        login = LoginPage(page)
        product = ProductsPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        assert product.verify_cart_icon()

        page.screenshot(path="screenshots/test_cart_icon_visibility.png")