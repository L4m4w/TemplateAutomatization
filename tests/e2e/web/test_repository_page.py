import pytest
import allure
from allure_commons.types import Severity

from pages.application import app
from configs.settings import user_data
from utils.decorators.common import step_for_allure


@pytest.mark.slow
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
def test_create_repository(browser_management, random_repository_data):
    app.login_page.open()
    app.login_page.login(user_data.email, user_data.password)
    app.home_page.create_repository.create_repository_sidebar_button.click()
    app.create_repository_page.enter_repository_name(
        random_repository_data['repository_name']
    )
    app.create_repository_page.enter_description(
        random_repository_data['description']
    )
    app.create_repository_page.choose_visibiltiy('private')
    app.create_repository_page.add_gitignore_and_choose_template(
        random_repository_data['gitignore_template']
    )
    app.create_repository_page.create_repository_button.click()

