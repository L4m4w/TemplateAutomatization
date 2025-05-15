from pages.application import app

def test_login_via_mail():
    app.login_page.open()
