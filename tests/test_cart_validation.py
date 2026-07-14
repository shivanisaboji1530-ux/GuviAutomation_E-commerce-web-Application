from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.cart_page import CartPage
from utils.config import USERNAME, PASSWORD


class TestCartValidation:

    def test_validate_cart_products(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)
        cart = CartPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        selected_products = products.select_random_products(4)

        products.open_cart()

        cart_products = cart.get_cart_products()

        assert len(cart_products) == 4

        print("\nProducts in Cart")

        for product in cart_products:
            print(product)

        page.screenshot(path="screenshots/test_validate_cart_products.png")