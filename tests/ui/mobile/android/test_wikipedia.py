from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
import pytest
import time

@pytest.mark.parametrize("title", ["BrowserStack", "Jira (software)"])
def test_wikipedia_search(title):
    pass
    # search_element = browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    # search_element.click()
    #
    # browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(title)
    #
    # result = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
    #
    # result.should(have.size_greater_than(0))
    # result.first.should(have.text(title))
    # time.sleep(10)