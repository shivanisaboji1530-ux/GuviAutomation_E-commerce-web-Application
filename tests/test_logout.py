from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from utils.config import USERNAME, PASSWORD


class TestLogout:

    def test_logout(self, page):

        login = LoginPage(page)
        menu = MenuPage(page)

        login.open_application()
        login.login(USERNAME, PASSWORD)

        menu.logout()

        assert "saucedemo.com" in page.url

        page.screenshot(path="screenshots/test_logout.png")