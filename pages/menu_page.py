from playwright.sync_api import Page


class MenuPage:

    MENU_BUTTON = "#react-burger-menu-btn"
    RESET_APP_STATE = "#reset_sidebar_link"
    LOGOUT = "#logout_sidebar_link"

    def __init__(self, page: Page):
        self.page = page

    def open_menu(self):
        self.page.locator(self.MENU_BUTTON).click()

    def reset_app_state(self):
        self.open_menu()
        self.page.locator(self.RESET_APP_STATE).wait_for(state="visible")
        self.page.locator(self.RESET_APP_STATE).click()

    def logout(self):
        self.open_menu()
        self.page.locator(self.LOGOUT).wait_for(state="visible")
        self.page.locator(self.LOGOUT).click()