from api.services.issues import IssueService
from configs.settings import user_data

def test_create_issue():
    issues = IssueService(token=user_data.git_token)

    issue = issues.create_issue(
        repo_owner=user_data.username,
        repo_name="Desiree-Leblanc",
        title='IIII'
    )

    assert issue["state"] == "open"

def test_get_issue():
    issues = IssueService(token=user_data.git_token)

    issue = issues.get_issue(
        repo_owner=user_data.username,
        repo_name="Desiree-Leblanc",
        issue_number='1'
    )

    assert issue["state"] == "open"
    assert issue["title"] == "IIII"
    assert issue["user"]["login"] == user_data.username
