from pages.application import app
from selene import browser


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
    assert browser.driver.current_url == 'https://trello.com/u/evge11/boards'

