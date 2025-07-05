from selene import browser, be, have

from configs.settings import user_data
from pages.application import app

from utils.utils_pages.utils_account import get_auth_cookie

def test_create_new_branch(browser_management):
    cookies = get_auth_cookie(user_data.email, user_data.password)
    app.branch_page.with_cookies(cookies).open()
    app.branch_page.create_new_branch()
    browser.element("div[title='321']").with_(timeout=10).should(be.visible)

def test_branch_name_already_exist(browser_management):
    cookies = get_auth_cookie(user_data.email, user_data.password)
    app.branch_page.with_cookies(cookies).open()
    app.branch_page.create_new_branch()
    app.branch_page.error_message_box.should(have.text('Sorry, that branch already exists.'))

def test_branch_in_branch_table(browser_management):
    cookies = get_auth_cookie(user_data.email, user_data.password)
    app.branch_page.with_cookies(cookies).open()
    # branch = app.branch_page.get_user_branch_from_table(321)
    branch = browser.element("div[title='321']")
    branch_link = branch.element('..')
    branch_link.should(have.attribute('href', "https://github.com/evgne/Desiree-Leblanc/tree/321"))
