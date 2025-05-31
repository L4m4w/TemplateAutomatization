from selene import by, be, browser

from pages.base_page import BasePage

class CreateRepositoryPage(BasePage):

    PAGE_URL = '/new'

    # def __init__(self, repository_name):
    #     self.repository_name = repository_name

    def enter_repository_name(self, repository_name):
        browser.element("#prc-components-Input-Ic-y8").element(by.id(":r5:"))
        browser.element(by.id(":r5:")).send_keys(repository_name)
        return self

    def enter_description(self, description):
        browser.element(by.id(":ra:")).send_keys(description)
        return self

    def choose_visibiltiy(self, visibility):
        radio_button_selector = \
            'input[name="visibilityGroup"][value="public"]' \
                if visibility == 'public' \
                else 'input[name="visibilityGroup"][value="private"]'
        browser.element(
            radio_button_selector
        ).click()
        return self

    @property
    def create_repository_button(self):
        browser.element('button:contains("Create repository")')
        return self