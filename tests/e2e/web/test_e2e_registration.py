from pages.application import app

def test_registration_by_email():

    app.registration.open()
    app.registration.email_signup.enter_email()
    app.registration.email_signup.email_signup_button.click()