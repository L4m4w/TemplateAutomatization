import requests
import allure
from curlify import to_curl
import json
import logging


def post_with_log(url, **kwargs):
    with allure.step(f"POST {url}"):
        response = requests.post(url=url, **kwargs)
        curl = to_curl(response.request)
        logging.info(response.json())
        logging.info(f'status code: {response.status_code}')
        logging.info(to_curl(response.request))
        allure.attach(body=curl, name='curl', attachment_type=allure.attachment_type.TEXT, extension="txt")
        allure.attach(body=json.dumps(response.json(), indent=4),
                      name='response',
                      attachment_type=allure.attachment_type.JSON, extension="json")
        return response

def get_with_log(url, **kwargs):
    with allure.step(f"POST {url}"):
        response = requests.get(url=url, **kwargs)
        curl = to_curl(response.request)
        logging.info(response.json())
        logging.info(to_curl(response.request))
        allure.attach(body=curl, name='curl', attachment_type=allure.attachment_type.TEXT, extension="txt")
        allure.attach(body=json.dumps(response.json(), indent=4),
                      name='response',
                      attachment_type=allure.attachment_type.JSON, extension="json")
        return response