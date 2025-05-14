from selene import by, be
from selene.support.conditions import have
from pages.base_page import BasePage

from selene import browser

class LoginPage(BasePage):
    def open(self):
        browser.open("/login")
        return self

    def login(self, email, password):
        browser.element("#userName").type(email)
        browser.element("#password").type(password)
        browser.element(by.id("login")).click()
        return self

    def assert_error_message(self, text):
        browser.element("#error").should(be.visible).should(have.text(text))
