from typing import Callable

import pytest
from selene import be, Browser
from selene.support.shared import browser

from tests.e2e.web.conftest import SupportedBrowsers


class TestLogin:
    @pytest.mark.platform("web")
    # @pytest.mark.platform("mobile")
    def test_something(self, with_new_browser: Callable[[SupportedBrowsers], Browser] | Callable[..., Browser]):
        browser.open('https://gfgf')
        browser.element('#new-todo').should(be.blank).type('a').press_enter()

        browser2 = with_new_browser(123)
        browser2.open('https://gfgf')
        browser2.element('#new-todo').should(be.blank).type('a').press_enter()

        browser3 = with_new_browser('firefox')
        browser3.open('https://gfgf')
        browser3.element('#new-todo').should(be.blank).type('a').press_enter()
