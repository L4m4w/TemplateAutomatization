import pytest
from selene import browser
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    ...
    # browser.config.timeout = 7.0
    # browser.config.base_url = "https://trello.com/"
    # browser.config.base_url = "https://github.com/"

    # browser.config.driver = webdriver.Chrome()

    # yield

    # browser.quit()

    # options = Options()
    # selenoid_capabilities = {
    #     "browserName": "firefox",
    #     "browserVersion": "138.0"
    # }
    # options.capabilities.update(selenoid_capabilities)



    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--start-maximized')
    #
    # driver_options.add_argument('--no-sandbox')
    # driver_options.add_argument('--disable-dev-shm-usage')
    # driver_options.add_argument('--headless')

    # browser.config.driver_options = driver_options
