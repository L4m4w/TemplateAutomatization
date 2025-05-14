from selene import browser
from login_page import LoginPage
# from profile_page import ProfilePage

class Application:
    def __init__(self):
        self.login_page = LoginPage()
        self.profile = ProfilePage()

app = Application()