from selene import by, be, browser

from pages.base_page import BasePage

class CreateRepositoryPage(BasePage):

    PAGE_URL = '/new'

    def enter_repository_name(self, text):
        ...