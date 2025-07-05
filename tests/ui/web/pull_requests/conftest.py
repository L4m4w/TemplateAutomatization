# import pytest
# from selene.support.shared import browser
# from selenium import webdriver
#
# from utils.utils_loggers import attach
#
# @pytest.fixture(scope='function', autouse=True)
# def browser_manager():
#     browser.config.base_url = 'https://github.com/'
#     browser.config.timeout = 4.0
#     browser.config.type_by_js = True
#
#     driver_options = webdriver.ChromeOptions()
#     driver_options.add_argument("--remote-debugging-port=9223")
#
#     browser.config.driver_options = driver_options
#
#     yield
#
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#
#     browser.quit()