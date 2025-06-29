from selene import browser, Config
from selenium.webdriver import ChromeOptions
import pytest
from selenium import webdriver

from utils.utils_loggers import attach
from utils.utils_data.test_data_factory import TestDataFactory

@pytest.fixture(scope='session')
def test_data():
    return TestDataFactory.generate_all_test_data(save_data=False)

@pytest.fixture()
def random_repository_data(test_data):
    import random
    return random.choice(test_data['repository_data'])

# # Автоматически запускается для всех функций, которые лежат в той же директории, что и конфтест
# @pytest.fixture(scope='function')
# def browser_management():
#     browser.config.timeout = 7.0
#     # browser.config.base_url = "https://trello.com/"
#     browser.config.base_url = "https://github.com/"
#
#
#     browser.config.driver = webdriver.Chrome()
#     driver_options = webdriver.ChromeOptions()
#     driver_options.add_argument('--start-maximized')
#
#     driver_options.add_argument('--no-sandbox')
#     driver_options.add_argument('--disable-dev-shm-usage')
#     # driver_options.add_argument('--headless')
#
#     yield
#
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#
#     browser.quit()


# def init_web_driver():
#     options = ChromeOptions()
#     options.add_argument("--headless")  # Для CI
#     browser.set_driver(Config(
#         driver_options=options,
#         timeout=10,
#         base_url="https://trello.com/"
#     ))

# def init_android_driver():
#     pass


# def pytest_addoption(parser):
#     parser.addoption("--platform", action="store", default="web")
#
# @pytest.fixture(scope='session')
# def platform(request):
#     return request.config.getoption("--platform")
#
# @pytest.fixture
# def driver(platform):
#     if platform == "web":
#         yield init_web_driver()
#     elif platform == "android":
#         yield init_android_driver()

