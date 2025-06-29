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
    driver_options = webdriver.ChromeOptions()

    # driver_options.add_argument("--headless=new")
    driver_options.add_argument("--enable-logging")
    driver_options.add_argument("--v=1")
    driver_options.add_argument("--no-sandbox")  # Важно для Linux/Docker!
    driver_options.add_argument("--disable-dev-shm-usage")  # Решает проблему с /dev/shm
    driver_options.add_argument("--remote-debugging-port=9222")  # Фиксированный порт

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    browser.quit()
