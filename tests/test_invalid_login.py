from pages.login_page import LoginPage


class TestInvalidLogin:

    def test_invalid_login(self, page):
        login = LoginPage(page)

        login.open_application()
        login.login("invalid_user", "invalid_password")

        assert login.get_error_message() == \
            "Epic sadface: Username and password do not match any user in this service"

        page.screenshot(path="screenshots/test_invalid_login.png")