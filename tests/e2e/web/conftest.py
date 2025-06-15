import pytest
from typing import Literal
from selene.support.shared import browser
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from utils.utils_loggers import attach


# Автоматически запускается для всех функций, которые лежат в той же директории, что и конфтест
@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 7.0
    # browser.config.base_url = "https://trello.com/"
    browser.config.base_url = "https://github.com/"


    browser.config.driver = webdriver.Chrome()

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()

SupportedBrowsers = Literal['chrome', 'firefox']

@pytest.fixture(scope='function')
def with_new_browser():
    future_browsers = []

    def new_browser(name: SupportedBrowsers = 'chrome'):
        nonlocal future_browsers
        if name == 'chrome':
            future_browser = (
                Browser(Config(driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())))))
        elif name == 'firefox':
            future_browser = (
                Browser(Config(driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())))))
        else:
            raise Exception(f'Browser <<{name}>> is not supported')

        future_browsers.append(future_browser)

        return future_browser

    yield new_browser

    for future_browser in future_browsers:
        future_browser.quit()
