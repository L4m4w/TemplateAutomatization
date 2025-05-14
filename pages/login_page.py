from selene import by, be
from selene.support.conditions import have

from conftest import browser

class LoginPage:
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
