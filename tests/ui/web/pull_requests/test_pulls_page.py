from selene import browser, be

from configs.settings import user_data
from pages.application import app

from utils.utils_pages.utils_account import get_auth_cookie

def test_1():
    cookies = get_auth_cookie(user_data.email, user_data.password)
    # app.home_page.open()
    #
    # for cookie in cookies:
    #     if cookie["domain"] in (".github.com", "github.com"):
    #         try:
    #             browser.driver.add_cookie(cookie)
    #         except Exception as e:
    #             print(f"Ошибка с кукой {cookie['name']}: {e}")
    #
    # app.branch_page.open()

    app.branch_page.with_cookies(cookies).open()

    app.branch_page.create_new_branch()
    browser.element("div[title='321']").with_(timeout=10).should(be.visible)
