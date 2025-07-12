import allure
import pytest
from allure_commons.types import Severity
from pydantic import ValidationError
from jsonschema import validate

from api.schemas.issue_schemas import GET_ISSUE_SCHEMA
from api.services.issues import IssueService
from api.models.Issue_models import IssueResponse
from configs.settings import user_data

@pytest.fixture
def issue_service():
    return IssueService(token=user_data.git_token)

@pytest.fixture
def issue_request_data():
    return {
        "repo_owner": user_data.username,
        "repo_name": user_data.repository_name,
        "issue_number": "1"
    }

@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Lamaw')
@allure.feature('Issues')
@allure.story('Create issue via API')
@allure.link('https://github.com', name='Testing')
@allure.description("""
Test check:
1. Ability to create issues with api
""")
def test_create_issue():
    issues = IssueService(token=user_data.git_token)

    issue = issues.create_issue(
        repo_owner=user_data.username,
        repo_name="Desiree-Leblanc",
        title='IIII'
    )
    with allure.step("Issue created with state 'open'"):
        assert issue["state"] == "open"

@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Lamaw')
@allure.feature('Issues')
@allure.story('Get issue via API')
@allure.link('https://github.com', name='Testing')
@allure.description("""
Test check:
1. Ability to get issues with api
""")
@pytest.mark.parametrize("issue_number, expected_state", [
    ("1", "open"),
])
def test_get_issue(issue_number, expected_state):
    issues = IssueService(token=user_data.git_token)

    issue = issues.get_issue(
        repo_owner=user_data.username,
        repo_name="Desiree-Leblanc",
        issue_number=issue_number
    )

    with allure.step("API returned issue and it has expected data"):
        assert issue["state"] == expected_state
        assert issue["title"] == "IIII3"
        assert issue["user"]["login"] == user_data.username

@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Lamaw')
@allure.feature('Issues')
@allure.story('Get issue via API')
@allure.link('https://github.com', name='Testing')
@allure.description("""
Test check:
1. API issue model equal to legacy issue model
""")
def test_get_issue_response_model(issue_service, issue_request_data):
    """
    Тест проверяет:
    - Ответ API соответствует модели IssueResponse.
    Ожидается прохождение проверки типов полей.
    """

    issue = issue_service.get_issue(**issue_request_data)

    validated_issue = IssueResponse(**issue)
    with allure.step("API issue model equal to legacy issue model"):
        assert isinstance(validated_issue, IssueResponse)

@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Lamaw')
@allure.feature('Issues')
@allure.story('Get issue via API')
@allure.link('https://github.com', name='Testing')
@allure.description("""
Test check:
1. API issue model equal to legacy issue model
""")
def test_get_issue_response_schema(issue_service, issue_request_data):
    issue = issue_service.get_issue(**issue_request_data)

    with allure.step("API issue schema equal to legacy issue model"):
        validate(issue, schema=GET_ISSUE_SCHEMA)

@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Lamaw')
@allure.feature('Issues')
@allure.story('Get validation error on requesting issue with wrong fields via API')
@allure.link('https://github.com', name='Testing')
@allure.description("""
Test check:
1. Validation error on requesting issue with wrong fields via API
""")
def test_invalid_issue_response():
    """
    Тест проверяет:
    - Ответ API в случае передачи 1 обязательного поля вместо 27.
    Ожидается получение ошибки валидации.
    """
    invalid_data = {"title": 123}
    with allure.step("Get validation error"):
        with pytest.raises(ValidationError) as exc_info:
            IssueResponse(**invalid_data)
    with allure.step("Response is invalid"):
        assert "validation errors for IssueResponse" in str(exc_info.value)
