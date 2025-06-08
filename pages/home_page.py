from selene import by, be, browser

from pages.base_page import BasePage

class HomePage(BasePage):

    PAGE_URL = ''

    class CreateRepository:

        @property
        def create_repository_sidebar_button(self):
            return browser.element(by.text("Create pull_requests"))

    create_repository = CreateRepository()



    @property
    def edit_workspace_name_button(self):
        return browser.element('.Ch1Opdvr77xkJp')