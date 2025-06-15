import json
import logging
import requests
from curlify import to_curl
import allure


class GithubAPIClient:
    def __init__(self, token, base_url="https://api.github.com"):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def _request(self, method, endpoint, **kwargs):
        with allure.step(f"{method} {endpoint}"):
                url = f"{self.base_url}{endpoint}"
                response = requests.request(method, url, headers=self.headers, **kwargs)
                curl = to_curl(response.request)
                logging.info(response.json())
                logging.info(to_curl(response.request))
                allure.attach(body=curl, name='curl', attachment_type=allure.attachment_type.TEXT, extension="txt")
                allure.attach(body=json.dumps(response.json(), indent=4),
                              name='response',
                              attachment_type=allure.attachment_type.JSON, extension="json")
                response.raise_for_status()
                return response.json() if response.content else None
