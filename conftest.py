import logging
import pytest
from playwright.sync_api import sync_playwright
from utils.config import Config
from utils.data_loader import DataLoader

# All fixtures should be stored here.

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p[Config.BROWSER].launch(headless=Config.HEADLESS)
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def login_data():
    return DataLoader().load_json("login_data.json")

@pytest.fixture(scope="session")
def base_url():
    return Config.BASE_URL

@pytest.fixture(scope="session")
def base_api_url():
    return Config.BASE_API_URL

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def logger():
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)
    return log