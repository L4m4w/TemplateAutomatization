import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from utils.utils_loggers import attach

#
# @pytest.fixture(scope='function')
# def browser_management():
#     browser.config.timeout = 7.0
#     browser.config.base_url = "https://github.com/"
#
#
#     chrome_options = Options()
#     chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument("--crash-dumps-dir=/tmp")
#     chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--disable-dev-shm-usage')
#     chrome_options.add_argument('--profile-directory=Default')
#     chrome_options.add_argument("--remote-debugging-port=9222")
#
#     browser.config.driver = webdriver.Chrome(options=chrome_options)
#
#     yield
#     # driver_options = webdriver.ChromeOptions()
#     #
#     # # driver_options.add_argument("--headless=new")
#     # driver_options.add_argument("--enable-logging")
#     # driver_options.add_argument("--v=1")
#     # driver_options.add_argument("--no-sandbox")  # Важно для Linux/Docker!
#     # driver_options.add_argument("--disable-dev-shm-usage")  # Решает проблему с /dev/shm
#     # driver_options.add_argument("--remote-debugging-port=9222")  # Фиксированный порт
#
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#
#     browser.quit()

@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://github.com/'
    browser.config.timeout = 4.0
    browser.config.type_by_js = True

    driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--start-maximized')
    # driver_options.add_argument('--no-sandbox')
    # driver_options.add_argument("--crash-dumps-dir=/tmp")
    # driver_options.add_argument('--headless')
    # driver_options.add_argument('--disable-gpu')
    # driver_options.add_argument('--disable-dev-shm-usage')
    # driver_options.add_argument('--profile-directory=Default')
    driver_options.add_argument("--remote-debugging-port=9222")

    browser.config.driver_options = driver_options

    yield

    browser.quit()