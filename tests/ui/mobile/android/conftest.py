import pytest
from appium.options.android import UiAutomator2Options
from selene import browser
import os

from configs.settings import user_data

from selenium import webdriver


@pytest.fixture(scope='module')
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": user_data.browserstack_username,
            "accessKey": user_data.browserstack_access_key
        }
    })

    # browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    browser.config.driver_remote_url = "http://hub.browserstack.com/wd/hub"
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '5.0'))

    yield

    browser.quit()
