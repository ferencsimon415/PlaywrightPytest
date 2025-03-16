import logging
import os
import pytest
from playwright.sync_api import sync_playwright, Page
from utils.config import Config
from utils.data_loader import DataLoader
from allure_commons.types import AttachmentType
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options

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


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, page: Page):
    yield
    # Only take screenshots for UI tests
    if "ui" in request.keywords and request.node.rep_call.failed:
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(
            screenshot_dir, f"{request.node.name}_failure.png"
        )

        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

        # Add screenshot to pytest report
        request.node.add_report_section(
            "call", "screenshot", f"[[file:{screenshot_path}]]"
        )

        # Add screenshot to Allure report
        with open(screenshot_path, "rb") as f:
            allure.attach(
                f.read(), name="failure_screenshot", attachment_type=AttachmentType.PNG
            )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def appdriver():
    options = UiAutomator2Options()
    options.platform_name = Config.PLATFORM_NAME
    options.device_name = Config.DEVICE_NAME
    options.app_package = Config.APP_PACKAGE
    options.app_activity = Config.APP_ACTIVITY
    options.automation_name = Config.AUTOMATION_NAME
    driver = webdriver.Remote(Config.APPIUM_URL, options=options)
    yield driver
    driver.quit()