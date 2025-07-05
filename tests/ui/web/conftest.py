import pytest
from selene.support.shared import browser
from selenium import webdriver

from utils.utils_loggers import attach

@pytest.fixture(scope='session')
@pytest.mark.parametrize("browsers", ["Chrome", "Firefox"])
@pytest.mark.parametrize("device", ["desktop", "mobile"])
def browser_management(request):
    print(request.param)
    browser.config.timeout = 7.0
    browser.config.base_url = "https://github.com"

    if request.param['browsers'] == "Chrome":
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument("--remote-debugging-port=9222")
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

@pytest.fixture(scope='function', params=["Chrome", "Firefox"])
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