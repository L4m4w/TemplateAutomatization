import time
from pathlib import Path

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
from selenium.webdriver.chrome.options import Options


from utils.utils_loggers import attach
from utils.utils_data.helpers import PROJECT_ROOT


SupportedBrowsers = Literal['chrome', 'firefox']


@pytest.fixture(scope='function')
@pytest.mark.parametrize("browsers", ["Chrome", "Firefox"])
@pytest.mark.parametrize("device", ["desktop", "mobile"])
def browser_management(request, base_url):
    browser.config.timeout = 7.0
    browser.config.base_url = base_url

    if request.param['browsers'] == "Chrome":
       browser_name = 'chrome'
       browser_version = '123.0'
    elif request.param['browsers'] == "Firefox":
        browser_name = 'firefox'
        browser_version = '123.0'
    else:
        raise NotImplementedError

    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version or None,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    if request.param['device'] == "desktop":
        options.add_argument("--window-size=1920,1080")
    elif request.param['device'] == "mobile":
        options.add_argument("--window-size=600,800")
    else:
        raise NotImplementedError

    host = '127.0.0.1' if Path(PROJECT_ROOT / ".env.local").exists() else 'selenoid'

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"http://{host}:4444/wd/hub",
        options=options
    )

    browser.config.driver = driver



    browser.config.options = options
    # browser.driver.get_log()

    yield browser

    attach.add_screenshot(browser)
    # attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()

@pytest.fixture(scope='module')
def with_new_browser():
    future_browsers = []

    def new_browser(name: SupportedBrowsers = 'Chrome'):
        nonlocal future_browsers
        if name == 'Chrome':
            future_browser = (
                Browser(Config(driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())))))
        elif name == 'Firefox':
            future_browser = (
                Browser(Config(driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())))))
        else:
            raise Exception(f'Browser <<{name}>> is not supported')

        future_browsers.append(future_browser)

        return future_browser

    yield new_browser

    for future_browser in future_browsers:
        future_browser.quit()
#
# @pytest.fixture(scope='function', autouse=True, params=["Chrome", "Firefox"])
# def mobile_browser_management(request):
#     browser.config.base_url = 'https://github.com'
#     if request.param == "Chrome":
#         driver_options = webdriver.ChromeOptions()
#     elif request.param == "Firefox":
#         driver_options = webdriver.FirefoxOptions()
#     else:
#         raise NotImplementedError
#     driver_options.browser_version = '100.0'
#     driver_options.set_capability(
#         'selenoid:options',
#         {
#             'screenResolution': '448x858x24'
#         },
#     )
#
#     browser.config.driver_options = driver_options
#
#     yield
#
#     browser.quit()

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