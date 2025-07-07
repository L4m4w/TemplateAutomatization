import time

import allure
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

SupportedBrowsers = Literal['chrome', 'firefox']





# Автоматически запускается для всех функций, которые лежат в той же директории, что и конфтест
@pytest.fixture(scope='session', autouse=True, params=["Chrome", "Firefox"])
def browser_management(request, base_url):
    browser.config.timeout = 7.0
    browser.config.base_url = base_url

    if request.param == "Chrome":
        browser.config.driver = webdriver.Chrome()
        driver_options = webdriver.ChromeOptions()
    elif request.param == "Firefox":
        browser.config.driver = webdriver.Firefox()
        driver_options = webdriver.FirefoxOptions()
    else:
        raise NotImplementedError


    driver_options.add_argument('--start-maximized')
    driver_options.add_argument("--remote-debugging-port=9222")

    driver_options.add_argument('--no-sandbox')
    driver_options.add_argument('--disable-dev-shm-usage')
    driver_options.add_argument('--incognito')

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()

@pytest.fixture(scope='module')
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

@pytest.fixture(scope='function', autouse=True, params=["Chrome", "Firefox"])
def mobile_browser_management(request):
    browser.config.base_url = 'https://github.com'
    if request.param == "Chrome":
        driver_options = webdriver.ChromeOptions()
    elif request.param == "Firefox":
        driver_options = webdriver.FirefoxOptions()
    else:
        raise NotImplementedError
    driver_options.browser_version = '100.0'
    driver_options.set_capability(
        'selenoid:options',
        {
            'screenResolution': '448x858x24'
        },
    )

    browser.config.driver_options = driver_options

    yield

    browser.quit()

def pytest_sessionstart(session):
    env = session.config.getoption("--env")
    allure.dynamic.label("environment", env)

def pytest_runtest_setup(item):
    item.start_time = time.time()

def pytest_runtest_teardown(item, nextitem):
    duration = time.time() - item.start_time
    print(f"\nТест {item.name} выполнялся {duration:.2f} сек")

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "slow: тесты, которые выполняются долго (mark as @pytest.mark.slow)"
    )
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     if outcome.get_result().failed:
#         browser.driver.save_screenshot(f"fail_{item.name}.png")