from selene import browser
from pages.auth.login_page import LoginPage
from pages.auth.registration_page import RegistrationPage
from pages.create_repository_page import CreateRepositoryPage
from pages.home_page import HomePage
# from profile_page import ProfilePage

class Application:
    def __init__(self):
        self.home_page = HomePage()
        self.login_page = LoginPage()
        self.registration = RegistrationPage()
        self.create_repository_page = CreateRepositoryPage()

    def open(self):
        browser.open('/')
        return self


app = Application()