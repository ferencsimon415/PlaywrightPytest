import pytest
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

@pytest.mark.mobile
def test_wifi_connectivity(appdriver):
    appdriver.implicitly_wait(10)
    #swipe the screen from top to middle
    appdriver.swipe(600,0,600,1200)
    sleep(2)
    appium_notification = appdriver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='android:id/notification_header'])[1]")
    assert appium_notification.get_attribute("enabled") == "true"
    #press home
    appdriver.press_keycode(3)
    sleep(2)