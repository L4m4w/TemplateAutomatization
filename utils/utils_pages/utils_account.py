import requests
import allure
from curlify import to_curl
import json
import logging
from selene import browser, have

from pages.application import app
from configs.settings import user_data

BASE_URL = 'https://github.com/'

@allure.step("Get auth cookie")
def get_cookie_api(acc_login: str, acc_password: str) -> str:
    response = requests.post(url=BASE_URL + 'login', data={"Email": acc_login, "Password": acc_password},
                             allow_redirects=False)
    curl = to_curl(response.request)
    allure.attach(body=response.cookies.get("NOPCOMMERCE.AUTH"), attachment_type=allure.attachment_type.TEXT, extension='txt')
    allure.attach(body=curl, attachment_type=allure.attachment_type.TEXT, extension='txt')
    return response.cookies.get("NOPCOMMERCE.AUTH")

@allure.step("Authorize")
def login_ui(acc_login: str, acc_password: str):
    browser.open(BASE_URL + "login")
    # Authorization: Bearer TRELLO_TOKEN
    browser.element("#login_field").send_keys(acc_login)
    browser.element("#password").send_keys(acc_password).press_enter()
    browser.element(".account").should(have.text())

def test_1():
    print(browser.config._get_base_url_on_open_with_no_args)