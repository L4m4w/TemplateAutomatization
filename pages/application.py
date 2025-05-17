from selene import browser
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.workspace_home_page import WorkspaceHomePage
# from profile_page import ProfilePage

class Application:
    def __init__(self):
        self.workspace_home_page = WorkspaceHomePage()
        self.login_page = LoginPage()
        self.registration = RegistrationPage()

    def open(self):
        browser.open('/')
        return self


app = Application()