from selene import browser, have
from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self):
        ...

    def open(self):
        browser.open(self.PAGE_URL)
        return self
