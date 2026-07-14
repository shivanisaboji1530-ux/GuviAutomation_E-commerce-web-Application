import random
from playwright.sync_api import Page, TimeoutError


class ProductsPage:

    CART_BADGE = ".shopping_cart_badge"
    CART_ICON = ".shopping_cart_link"
    PRODUCT_SORT = ".product_sort_container"

    def __init__(self, page: Page):
        self.page = page

    def select_random_products(self, count):
        products = self.page.locator(".inventory_item")
        total_products = products.count()

        random_indexes = random.sample(range(total_products), count)

        selected_products = []

        for index in random_indexes:
            product = products.nth(index)

            product_name = product.locator(".inventory_item_name").text_content().strip()
            selected_products.append(product_name)

            product.locator("button").click()

        return selected_products

    def open_cart(self):
        self.page.locator(self.CART_ICON).click()

    def verify_cart_badge(self):
        try:
            badge = self.page.locator(self.CART_BADGE)
            return badge.text_content(timeout=1000).strip()
        except TimeoutError:
            return "0"

    def verify_cart_icon(self):
        return self.page.locator(self.CART_ICON).is_visible()

    def sort_products(self, option):
        self.page.locator(self.PRODUCT_SORT).select_option(label=option)

    def verify_name_a_to_z(self):
        names = self.page.locator(".inventory_item_name").all_text_contents()
        return names == sorted(names)

    def verify_name_z_to_a(self):
        names = self.page.locator(".inventory_item_name").all_text_contents()
        return names == sorted(names, reverse=True)

    def verify_price_low_to_high(self):
        prices = [
            float(price.replace("$", ""))
            for price in self.page.locator(".inventory_item_price").all_text_contents()
        ]
        return prices == sorted(prices)

    def verify_price_high_to_low(self):
        prices = [
            float(price.replace("$", ""))
            for price in self.page.locator(".inventory_item_price").all_text_contents()
        ]
        return prices == sorted(prices, reverse=True)