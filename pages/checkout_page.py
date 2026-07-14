from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.checkout_btn = page.locator("#checkout")
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    def click_checkout(self):
        self.checkout_btn.click()

    def enter_checkout_details(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_btn.click()

    def take_screenshot(self):
        self.page.screenshot(path="screenshots/checkout.png")

    def finish_order(self):
        self.finish_btn.click()

    def verify_order_success(self):
        return self.success_message.text_content().strip() == "Thank you for your order!"