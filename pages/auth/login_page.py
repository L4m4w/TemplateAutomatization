import time

from selene import by, be, browser
from selene.support.conditions import have

from pages.base_page import BasePage
from configs.settings import user_data

from selenium.webdriver.remote.webelement import WebElement



class LoginPage(BasePage):

    PAGE_URL = 'login'

    def login(self, email, password):
        browser.element("#login_field").type(email)
        browser.element("#password").type(password)
        browser.element(by.name("commit")).press_enter()
        return self

    def assert_error_message(self, text):
        browser.element("#error").should(be.visible).should(have.text(text))

    class EmailLogin:

        email = user_data.email
        password = user_data.password

        @property
        def email_login_button(self) -> WebElement:
            return browser.element('#login-submit')

        @property
        def email_login_continue_button(self):
            return browser.element('#login-submit')

        def enter_email(self, email = email):
            browser.element('#email').type(email)

        def enter_password(self, password=password):
            browser.element('#password').type(password)

    email_login = EmailLogin()