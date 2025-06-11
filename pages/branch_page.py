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
        input_field = self.new_branch_name_field
        input_field.should(be.visible.and_(be.enabled))
        input_field.click()
        input_field.send_keys('321')
        self.create_new_branch_button.click()

    def error_message_box(self):
        error_box = browser.element('div[id="flash"]')
        return error_box.element('.//div')

    @property
    def new_branch_name_field(self):
        form = browser.element('div[class="prc-Dialog-Body-LCvER"]')
        return form.element('.//input')

    @property
    def create_new_branch_button(self):
        return browser.element('button[class="prc-Button-ButtonBase-c50BI"][data-variant="primary"][aria-describedby*="loading-announcement"]')

    @property
    def user_branches_table(self):
        return browser.element('table[aria-labelledby="yours"]')