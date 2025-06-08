from selene import by, be, browser

from pages.base_page import BasePage
from configs.settings import user_data

class BranchPage(BasePage):

    PAGE_URL = f'{user_data.username}/{user_data.repository_name}/branches'

    @property
    def new_branch_button(self):
        return browser.element('button[class="prc-Button-ButtonBase-c50BI ml-3"]')

    def create_new_branch(self):
        self.new_branch_button.click()
        self.new_branch_name_field.send_keys('master')
        self.create_new_branch_button.click()

    @property
    def new_branch_name_field(self):
        return browser.element('input[class="prc-components-Input-Ic-y8"]')

    @property
    def create_new_branch_button(self):
        return browser.element('button[class="prc-Button-ButtonBase-c50BI"][aria-describedby=":r3c:-loading-announcement"]')
