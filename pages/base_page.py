from selene import browser, have
from abc import ABC, abstractmethod


class BasePage(ABC):
    home_page=''

    def __init__(self):
        ...

    def open(self):
        browser.open(self.PAGE_URL)
        return self

    def with_cookies(self, cookies):
        browser.open('https://github.com')

        for cookie in cookies:
            if cookie["domain"] in (".github.com", "github.com"):
                try:
                    browser.driver.add_cookie(cookie)
                except Exception as e:
                    print(f"Ошибка с кукой {cookie['name']}: {e}")

        self.open()
        return self
