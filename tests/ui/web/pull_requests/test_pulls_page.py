from selene import browser, be, have

from configs.settings import user_data
from pages.application import app

from utils.utils_pages.utils_account import get_auth_cookie

def test_create_new_branch():
    cookies = get_auth_cookie(user_data.email, user_data.password)

    app.branch_page.with_cookies(cookies).open()

    app.branch_page.create_new_branch()
    browser.element("div[title='321']").with_(timeout=10).should(be.visible)

def test_branch_name_already_exist():
    cookies = get_auth_cookie(user_data.email, user_data.password)
    app.branch_page.with_cookies(cookies).open()
    app.branch_page.create_new_branch()
    app.branch_page.error_message_box().should(have.text('Sorry, that branch already exists.'))

