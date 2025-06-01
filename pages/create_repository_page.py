from selene import by, have, browser
from selene.support.conditions.be import clickable

from pages.base_page import BasePage

class CreateRepositoryPage(BasePage):

    PAGE_URL = '/new'

    # def __init__(self, repository_name):
    #     self.repository_name = repository_name

    def enter_repository_name(self, repository_name):
        # browser.element("#prc-components-Input-Ic-y8").element(by.id(":r5:"))
        # browser.element('input').and_(have.css_property('aria-describedby="RepoNameInput-is-available'))
        browser.element('input[aria-required="true"][aria-describedby*="RepoNameInput"]').send_keys(repository_name)
        # browser.element(by.id(":r5:")).send_keys(repository_name)
        return self

    def enter_description(self, description):
        # browser.element(by.id(":ra:")).send_keys(description)
        browser.element('input[aria-label="Description"]').send_keys(description)
        return self

    def add_readme_file(self):
        browser.element('#:ri:').click()
        return self

    def add_gitignore_and_choose_template(self, template_name: str = 'None'):
        # browser.element(by.id(':rm:')).click()
        browser.element('button[aria-describedby*="license-picker-label"]').click()
        # template_list = browser.element(by.id("#\:rl1\:"))
        browser.element('input[role="combobox"][placeholder="Filter…"]').send_keys(template_name).press_enter()


        # dropdown_list = browser.element('#\\:rb8\\:')

        # list_items = template_list.all('li.prc-ActionList-ActionListItem-uq6I7')

        # list_items.element_by(
        #     have.css_class('span.prc-ActionList-ItemLabel-TmBhn').and_(have.text(template_name))
        # ).click()

        # list_items.element_by(have.text(template_name)).click()
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
        return browser.element('button[type="submit"][aria-describedby*="-loading-announcement"]')
