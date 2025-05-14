from selene import browser
from pages.login_page import LoginPage
from pages.workspace_home_page import WorkspaceHomePage
# from profile_page import ProfilePage

class Application:
    def __init__(self):
        self.login_page = LoginPage()
        self.workspace_home_page = WorkspaceHomePage()

    def open(self):
        browser.open('/')
        return self


app = Application()