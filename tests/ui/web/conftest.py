import pytest
from selene.support.shared import browser
from selenium import webdriver

from utils.utils_loggers import attach


@pytest.fixture(scope='module')
def browser_management():
    browser.config.timeout = 7.0
    browser.config.base_url = "https://github.com/"

    # browser.config.driver = webdriver.Chrome()

    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument("--remote-debugging-port=9222")

    browser.config.driver_options = driver_options

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()
