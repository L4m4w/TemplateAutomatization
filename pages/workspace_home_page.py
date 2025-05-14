from selene.support.shared import browser

from pages.base_page import BasePage

class WorkspaceHomePage(BasePage):

    PAGE_URL = 'w/tacoco129/home'

    def open(self):
        browser.open(self.PAGE_URL)
        return self

    @property
    def edit_workspace_name_button(self):
        return browser.element('.Ch1Opdvr77xkJp')