from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def get_cart_products(self):
        return [item.strip() for item in self.cart_items.all_text_contents()]

    def click_checkout(self):
        self.checkout_button.click()

    def click_continue_shopping(self):
        self.continue_shopping_button.click()