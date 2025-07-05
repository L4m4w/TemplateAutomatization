# import pytest
# from selene import browser, by, be
# from selenium import webdriver
#
#
#
# @pytest.fixture(scope="module")
# @pytest.mark.parametrize("browsers", ["Chrome", "Firefox"])
# @pytest.mark.parametrize("device", ["desktop", "mobile"])
# def browser_manager(request):
#     browser.config.base_url = 'https://github.com'
#     driver_options = webdriver.ChromeOptions()
#
#     driver_options.add_argument("--remote-debugging-port=9224")
#
#     browser.config.timeout = 2.0
#     if request.param == "desktop":
#         driver_options.add_argument("--window-size=1920,1080")
#     elif request.param == "mobile":
#         driver_options.add_argument("--window-size=600,800")
#
#
#
#     browser.config.driver_options = driver_options
#
#     yield
#
#     browser.quit()
