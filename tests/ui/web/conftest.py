import time

import allure
import pytest
from selene.support.shared import browser
from selenium import webdriver

from utils.utils_loggers import attach



@pytest.fixture(scope='function')
@pytest.mark.parametrize("browsers", ["Chrome", "Firefox"])
@pytest.mark.parametrize("device", ["desktop", "mobile"])
def browser_management(request, base_url):
    browser.config.timeout = 7.0
    browser.config.base_url = base_url

    if request.param['browsers'] == "Chrome":
        driver_options = webdriver.ChromeOptions()
        # driver_options.add_argument("--remote-debugging-port=9222")
    elif request.param['browsers'] == "Firefox":
        driver_options = webdriver.FirefoxOptions()
    else:
        raise NotImplementedError

    if request.param['device'] == "desktop":
        driver_options.add_argument("--window-size=1920,1080")
    elif request.param['device'] == "mobile":
        driver_options.add_argument("--window-size=600,800")
    else:
        raise NotImplementedError

    browser.config.driver_options = driver_options

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
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