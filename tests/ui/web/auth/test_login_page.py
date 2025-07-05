import os
import shutil

import allure
from allure_commons.types import Severity
from selene import browser
import pytest

from utils.decorators.common import step_for_allure
from utils.utils_pages.utils_account import login_ui
from configs.settings import user_data
from pages.application import app

@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Lamaw')
@allure.feature('Authorization')
@allure.story('Unauthorized user can authorize')
@allure.link('https://github.com', name='Testing')
@allure.description("""
Test check:
1. Ability to login with correct credentials
2. Visibility of user page after login
""")
@step_for_allure
@pytest.mark.parametrize("browser_management", [{"browsers": "Chrome", "device": "desktop"}], indirect=True)
def test_successful_login(browser_management):
    app.login_page.open()
    app.login_page.login(user_data.email, user_data.password)
    app.login_page.check_login_status(login=True)

@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Lamaw')
@allure.feature('Authorization')
@allure.title("Check bad auth with wrong credentials")
@allure.story('Bad auth')
@allure.link('https://github.com', name='Testing')
@allure.description("""
Test check:
1. Disability to login with incorrect credentials
2. Visibility of bad auth error
""")
@step_for_allure
@pytest.mark.parametrize("browser_management", [{"browsers": "Chrome", "device": "desktop"}], indirect=True)
def test_invalid_password_shows_error(browser_management):
    app.login_page.open()
    # app.login_page.login(user_data.email,user_data.username)
    app.login_page.assert_error_message('Incorrect username or password')