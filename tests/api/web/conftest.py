import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.timeout = 3.0
    browser.config.base_url="https://trello.com/"

    yield

    browser.quit()