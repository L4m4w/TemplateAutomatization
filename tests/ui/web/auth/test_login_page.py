import os
import shutil

from utils.utils_pages.utils_account import login_ui
from configs.settings import user_data
from pages.application import app

def test_successful_login():
    app.login_page.open()
    app.login_page.login(user_data.email, user_data.password)
    app.login_page.check_login_status(login=True)


def test_invalid_password_shows_error():
    app.login_page.open()
    app.login_page.login(user_data.email,user_data.username)
    app.login_page.assert_error_message('Incorrect username or password')