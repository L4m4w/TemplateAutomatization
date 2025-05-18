from selene import browser

from pages.base_page import BasePage
from configs.settings import user_data

class BoardPage(BasePage):

    PAGE_URL = f'u/{user_data.username}/boards'

    def create_board(self, by_template):
        browser.element('.jKBWU1uXSMBpHL MAZAn6WpFmeGh0').click()