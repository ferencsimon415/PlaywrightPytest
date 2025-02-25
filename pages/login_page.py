from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
    
    def enter_credentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
    
    def click_login(self):
        self.login_button.click()