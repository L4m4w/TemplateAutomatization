import time
from pathlib import Path

import allure
import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from utils.utils_loggers import attach
from utils.utils_data.helpers import PROJECT_ROOT


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

    host = '127.0.0.1' if Path(PROJECT_ROOT / ".env.local").exists() else 'selenoid'

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"http://{host}:4444/wd/hub",
        options=options
    )

    browser.config.driver = driver

    if request.param['device'] == "desktop":
        options.add_argument("--window-size=1920,1080")
    elif request.param['device'] == "mobile":
        options.add_argument("--window-size=600,800")
    else:
        raise NotImplementedError

    browser.config.options = options
    # browser.driver.get_log()

    yield browser

    attach.add_screenshot(browser)
    # attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()

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

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     if outcome.get_result().failed:
#         browser.driver.save_screenshot(f"fail_{item.name}.png")