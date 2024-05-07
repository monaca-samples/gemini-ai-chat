import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.example.framework7',
    appActivity='.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_gemi(self) -> None:
        input_element = driver.find_element(MobileBy.XPATH, '//android.widget.EditText')
        input_element.send_keys('What is the capital of Japan?')
        link = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Send"]')
        link.click()
        time.sleep(2)  # wait for 2 seconds
        text_element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Tokyo"]')

        # wait up to 5 seconds for the text element to exist
        for _ in range(5):
            if text_element.is_displayed():
                break
            time.sleep(1)

        text = text_element.text

        if text == 'Tokyo':
            print('Text "Tokyo" found')
        else:
            print('Text "Tokyo" not found')

if __name__ == '__main__':
    unittest.main()