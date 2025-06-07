import pytest
from pydantic import ValidationError

from api.services.issues import IssueService
from api.models.Issue_models import IssueResponse
from configs.settings import user_data

@pytest.fixture
def issue_service():
    return IssueService(token=user_data.git_token)

@pytest.fixture
def get_issue_data():
    return {
        "repo_owner": user_data.username,
        "repo_name": user_data.repository_name,
        "issue_number": "1"
    }

def test_create_issue():
    issues = IssueService(token=user_data.git_token)

    issue = issues.create_issue(
        repo_owner=user_data.username,
        repo_name="Desiree-Leblanc",
        title='IIII'
    )

    assert issue["state"] == "open"

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

    assert issue["state"] == expected_state
    assert issue["title"] == "IIII"
    assert issue["user"]["login"] == user_data.username

def test_get_issue_response_model(issue_service, get_issue_data):
    """
    Тест проверяет:
    1. Ответ API соответствует модели IssueResponse.
    Ожидается прохождение проверки типов полей.
    """

    issue = issue_service.get_issue(**get_issue_data)

    # try:
    #     model = IssueResponse(**issue)
    # except ValidationError as exc:
    #     print(repr(exc.errors()))

    validated_issue = IssueResponse(**issue)
    assert isinstance(validated_issue, IssueResponse)

def test_invalid_issue_response():
    """
    Тест проверяет:
    Ответ API в случае передачи 1 обязательного поля вместо 27.
    Ожидается получение ошибки валидации.
    """
    invalid_data = {"title": 123}  # Невалидные данные (title должен быть строкой)
    with pytest.raises(ValidationError) as exc_info:
        IssueResponse(**invalid_data)
    assert "validation errors for IssueResponse" in str(exc_info.value)