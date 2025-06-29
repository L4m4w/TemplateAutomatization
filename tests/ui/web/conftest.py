import pytest
from selene.support.shared import browser
from selenium import webdriver

from utils.utils_loggers import attach


@pytest.fixture(scope='module')
def browser_management():
    browser.config.timeout = 7.0
    browser.config.base_url = "https://github.com/"

    browser.config.driver = webdriver.Chrome()

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()
