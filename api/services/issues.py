from api.api_client import GithubAPIClient

class IssueService(GithubAPIClient):
    def create_issue(self, repo_owner, repo_name, title, body=None):
        endpoint = f"/repos/{repo_owner}/{repo_name}/issues"
        payload = {"title": title, "body": body}
        return self._request("POST", endpoint, json=payload)

    def get_issue(self, repo_owner, repo_name, issue_number):
        endpoint = f"/repos/{repo_owner}/{repo_name}/issues/{issue_number}"
        return self._request("GET", endpoint)

    def close_issue(self, repo_owner, repo_name, issue_number):
        endpoint = f"/repos/{repo_owner}/{repo_name}/issues/{issue_number}"
        return self._request("PATCH", endpoint, json={"state": "closed"})