from selene import browser, Config
from selenium.webdriver import ChromeOptions
import pytest

def init_web_driver():
    options = ChromeOptions()
    options.add_argument("--headless")  # Для CI
    browser.set_driver(Config(
        driver_options=options,
        timeout=10,
        base_url="https://trello.com/"
    ))

def init_android_driver():
    pass


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="web")

@pytest.fixture(scope='session')
def platform(request):
    return request.config.getoption("--platform")

@pytest.fixture
def driver(platform):
    if platform == "web":
        yield init_web_driver()
    elif platform == "android":
        yield init_android_driver()
