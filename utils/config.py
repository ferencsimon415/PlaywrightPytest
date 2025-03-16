class Config:
    ### UI

    BASE_URL = "https://www.automationexercise.com/"
    BASE_API_URL = "https://automationexercise.com/api/"
    BROWSER = "chromium"
    HEADLESS = False
    TIMEOUT = 10000

    ### Mobile

    PLATFORM_NAME = "android"
    DEVICE_NAME = "emulator-5554"
    APP_PACKAGE = "com.android.chrome"
    APP_ACTIVITY = "com.google.android.apps.chrome.Main"
    AUTOMATION_NAME = "UiAutomator2"
    APPIUM_URL = "http://127.0.0.1:4723"