from selene import by, be, browser

from pages.base_page import BasePage
from configs.settings import user_data

class PullsPage(BasePage):

    PAGE_URL = f'{user_data.username}/{user_data.repository_name}/pulls'

