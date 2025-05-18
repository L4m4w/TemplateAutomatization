from selene import browser

from pages.application import app
from configs.settings import user_data


def test_registration_by_email():

    app.registration.open()
    app.registration.email_signup.enter_email()
    app.registration.email_signup.email_signup_button.click()
    app.registration.email_signup.process_captcha()
    app.registration.email_signup.email_signup_button.click()
    app.login_page.email_login.email_login_continue_button.click()
    app.login_page.email_login.enter_password()
    app.login_page.email_login.email_login_button.click()
    # print(browser.driver.current_url)
    assert (browser.driver.current_url ==
            f'https://trello.com/u/{user_data.username}/boards')

