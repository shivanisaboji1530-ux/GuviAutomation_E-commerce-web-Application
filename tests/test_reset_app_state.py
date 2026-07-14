from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.menu_page import MenuPage
from utils.config import USERNAME, PASSWORD


class TestResetAppState:

    def test_reset_app_state(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)
        menu = MenuPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        products.select_random_products(4)

        assert products.verify_cart_badge() == "4"

        menu.reset_app_state()

        assert products.verify_cart_badge() == "0"

        page.screenshot(path="screenshots/test_reset_app_state.png")

