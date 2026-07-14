from utils.config import URL


class LoginPage:

    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "h3[data-test='error']"

    def __init__(self, page):
        self.page = page

    def open_application(self):
        self.page.goto(URL)

    def login(self, username, password):
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    def is_login_page_displayed(self):
        return self.page.locator(self.LOGIN_BUTTON).is_visible()