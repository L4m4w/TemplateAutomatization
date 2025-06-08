import pytest
from selene.support.shared import browser
from selenium import webdriver



@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 7.0
    browser.config.base_url = "https://github.com/"

    browser.config.driver = webdriver.Chrome()

    yield

    browser.quit()
