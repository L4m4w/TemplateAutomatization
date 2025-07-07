import allure
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


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="prod",
        choices=["prod", "stage", "dev"],
        help="Set test environment: prod, stage, dev"
    )

@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope='session')
def base_url(env):
    env_urls = {
        'prod': 'https://github.com/',
        'stage': 'https://stage-github.com/',
        'dev': 'https://dev-github.com/'
    }
    url = env_urls[env]
    allure.dynamic.link(url, name=f"{env} environment")
    return url