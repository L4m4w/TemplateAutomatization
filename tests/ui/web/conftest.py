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
        # browser.config.driver = webdriver.Chrome()
        # driver_options = webdriver.ChromeOptions()
        # driver_options.add_argument("--remote-debugging-port=9222")
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless=new')
        # additional options:
        options.add_argument("--remote-debugging-port=9222")

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-infobars')
        options.add_argument('--enable-automation')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-setuid-sandbox')
        browser.config.driver_options = options
    elif request.param['browsers'] == "Firefox":
        browser.config.driver = webdriver.Firefox()
        options = webdriver.FirefoxOptions()
    else:
        raise NotImplementedError

    if request.param['device'] == "desktop":
        options.add_argument("--window-size=1920,1080")
    elif request.param['device'] == "mobile":
        options.add_argument("--window-size=600,800")
    else:
        raise NotImplementedError

    browser.config.driver_options = options

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