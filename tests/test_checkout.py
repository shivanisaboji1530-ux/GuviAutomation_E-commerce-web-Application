from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from pages.checkout_page import CheckoutPage
from utils.config import USERNAME, PASSWORD


class TestCheckout:

    def test_checkout_process(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)
        checkout = CheckoutPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        products.select_random_products(4)

        products.open_cart()

        checkout.click_checkout()

        checkout.enter_checkout_details(
            "Shivani",
            "Saboji",
            "580020"
        )

        checkout.take_screenshot()

        checkout.finish_order()

        assert checkout.verify_order_success()

        page.screenshot(path="screenshots/test_checkout_process.png")