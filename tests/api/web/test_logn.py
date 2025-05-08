import pytest
from selene import have, be, Browser, Config
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class TestLogin:
    @pytest.mark.platform("web")
    @pytest.mark.platform("mobile")
    def test_something(self, with_new_browser):
        browser.open('https://gfgf')
        browser.element('#new-todo').should(be.blank).type('a').press_enter()

        browser2 = with_new_browser()
        browser2.open('https://gfgf')
        browser2.element('#new-todo').should(be.blank).type('a').press_enter()

        browser3 = with_new_browser('firefox')
        browser3.open('https://gfgf')
        browser3.element('#new-todo').should(be.blank).type('a').press_enter()
