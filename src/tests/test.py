import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        wait = WebDriverWait(self.driver, 600)  # wait up to 600 seconds
        self.driver.get_screenshot_as_file('screenshot_initial_state.png')
        input_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
        input_element.click()
        input_element.send_keys('What is the capital of Japan?')
        self.driver.get_screenshot_as_file('screenshot_after_input.png')
        link = wait.until(EC.presence_of_element_located((AppiumBy.XPATH,  '//*[@text="Send"]')))
        link.click()
        text_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Tokyo"]')))
        self.driver.get_screenshot_as_file('screenshot_after_response.png')
        text = text_element.text
        if text == 'Tokyo':
            print('Text "Tokyo" found')
        else:
            print('Text "Tokyo" not found')

if __name__ == '__main__':
    unittest.main()
