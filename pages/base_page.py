from selene import browser, have
from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def open(self):
        ...
