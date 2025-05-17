from selene import browser

from pages.base_page import BasePage

class RegistrationPage(BasePage):

    PAGE_URL = 'signup'

    # def __init__(self):

        # self.email_signup_button = browser.element('#signup-submit')


    class EmailSignup:

        email = 'evgne1334@outlook.com'
        password = 'j.}qj2g2V}>38^6'

        @property
        def email_signup_button(self):
            return browser.element('#signup-submit')

        @property
        def email_signup_continue_button(self):
            return browser.element('#login-submit')

        def enter_email(self, email = email):
            browser.element('#email').type(email)

        def enter_password(self, password=password):
            browser.element('#email').type(password)



    class GoogleSignup:

        @property
        def google_signup_button(self):
            return browser.element('#google-auth-button')

    class MicrosoftSignup:

        @property
        def microsoft_signup_button(self):
            return browser.element('#microsoft-auth-button')

    class AppleSignup:

        @property
        def apple_signup_button(self):
            return browser.element('#apple-auth-button')

    class SlackSignup:

        @property
        def slack_signup_button(self):
            return browser.element('#slack-auth-button')

    @property
    def login_redirect_by_already_have_an_account(self):
        return browser.element('#already-have-an-account')

    @property
    def cloud_terms_of_service_redirect_button(self):
        return browser.element(
            '#form-sign-up > div.css-1gu5jds > p > a:nth-child(1) > span._19itglyw._vchhusvi._r06hglyw._1e0c1nu9._o5721q9c._s7n4jp4b._kqswh2mm._152ttb3r > svg')

    @property
    def privacy_policy_redirect_button(self):
        return browser.element(
            '#form-sign-up > div.css-1gu5jds > p > a:nth-child(2)')

    email_signup = EmailSignup()
    google_signup = GoogleSignup()
    microsoft_signup = MicrosoftSignup()
    apple_signup = AppleSignup()
    slack_signup = SlackSignup()


