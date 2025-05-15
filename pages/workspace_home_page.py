from selene import browser

from pages.base_page import BasePage

class WorkspaceHomePage(BasePage):

    PAGE_URL = 'w/tacoco129/home'

    def open(self, url = PAGE_URL):
        browser.open(url)
        return self

    @property
    def edit_workspace_name_button(self):
        return browser.element('.Ch1Opdvr77xkJp')