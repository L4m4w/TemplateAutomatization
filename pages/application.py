from selene import browser
from pages.auth.login_page import LoginPage
from pages.auth.registration_page import RegistrationPage
from pages.main_page import HomePage
# from profile_page import ProfilePage

class Application:
    def __init__(self):
        self.workspace_home_page = HomePage()
        self.login_page = LoginPage()
        self.registration = RegistrationPage()

    def open(self):
        browser.open('/')
        return self


app = Application()