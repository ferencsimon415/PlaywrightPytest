from playwright.sync_api import Page

# Use this as super, for all other page objects.

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url):
        self.page.goto(url)
    
    def get_title(self):
        return self.page.title()
    
    def wait_for_element(self, selector):
        return self.page.wait_for_selector(selector)
    
    def accept_data_privacy(self):
        try:
            self.page.get_by_role("button", name="Beleegyezés").click()
        except Exception as e:
            print(e)