from pages.login_page import LoginPage
from playwright.sync_api import expect

from pages.main_page import MainPage

### helper methods ###

def navigate_to_login_screen(page, base_url):
    login_page = LoginPage(page)
    login_page.navigate(f"{base_url}/login")
    login_page.accept_data_privacy()
    return login_page

### tests ###

def test_successful_login(page, base_url, login_data):
    login_page = navigate_to_login_screen(page, base_url)
    login_page.enter_credentials(username = login_data['valid_credentials']['username'], password = login_data['valid_credentials']['password'])
    login_page.click_login()
    expect(page).to_have_url(base_url)
    
def test_login_with_bad_credentials(page, base_url, login_data):
    login_page = navigate_to_login_screen(page, base_url)
    login_page.enter_credentials(username = login_data['invalid_credentials'][0]['username'], password = login_data['invalid_credentials'][0]['password'])
    login_page.click_login()
    expect(page.locator("#form")).to_contain_text("Your email or password is incorrect!")

def test_logout(page, base_url, login_data):
    main_page = MainPage(page)
    login_page = navigate_to_login_screen(page, base_url)
    login_page.enter_credentials(username = login_data['valid_credentials']['username'], password = login_data['valid_credentials']['password'])
    login_page.click_login()
    expect(page).to_have_url(base_url)
    main_page.click_logout()
    expect(page).to_have_url(f"{base_url}login")
