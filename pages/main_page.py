from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logout_button = page.get_by_role("link", name=" Logout")

    def click_logout(self):
        self.logout_button.click()