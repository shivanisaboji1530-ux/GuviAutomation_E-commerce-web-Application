from pages.login_page import LoginPage
from pages.product_page import ProductsPage
from utils.config import USERNAME, PASSWORD


class TestRandomProducts:

    def test_random_product_selection(self, page):

        login = LoginPage(page)
        products = ProductsPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        selected_products = products.select_random_products(4)

        print("\nSelected Products")
        print("-" * 40)

        for index, product in enumerate(selected_products, start=1):
            print(f"{index}. {product}")

        print("-" * 40)

        assert len(selected_products) == 4