from selene import by, be
from selene.support.conditions import have
from pages.base_page import BasePage

from selene import browser

class LoginPage(BasePage):

    PAGE_URL = 'login'

    def login(self, email, password):
        browser.element("#userName").type(email)
        browser.element("#password").type(password)
        browser.element(by.id("login")).click()
        return self

    def assert_error_message(self, text):
        browser.element("#error").should(be.visible).should(have.text(text))

    class EmailLogin:

        email = 'evgne1334@outlook.com'
        password = 'j.}qj2g2V}>38^6'

        @property
        def email_login_button(self):
            return browser.element('#login-submit')

        @property
        def email_login_continue_button(self):
            return browser.element('#login-submit')

        def enter_email(self, email = email):
            browser.element('#email').type(email)

        def enter_password(self, password=password):
            browser.element('#email').type(password)

    email_login = EmailLogin()