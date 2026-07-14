from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from utils.config import USERNAME, PASSWORD


class TestAddToCart:

    def test_add_products_to_cart(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        products.select_random_products(4)

        assert products.verify_cart_badge() == "4"

        page.screenshot(path="screenshots/test_add_product_to_cart.png")