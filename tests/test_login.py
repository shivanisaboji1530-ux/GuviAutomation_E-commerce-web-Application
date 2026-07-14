from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


class TestLogin:

    def test_valid_login(self, page):
        login = LoginPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        assert "inventory.html" in page.url

        page.screenshot(path="screenshots/test_valid_login.png")