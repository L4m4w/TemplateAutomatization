from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import pytest

# @pytest.mark.parametrize("title", ["BrowserStack", "Jira (software)"])
def test_wikipedia_search():

    search_element = browser.element((AppiumBy.ACCESSIBILITY_ID, "The DuckDB Local UI"))
    search_element.click()

    # browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(title)

    result = browser.all((AppiumBy.CLASS_NAME, "XCUIElementTypeStaticText"))

    # result.should(have.size_greater_than(0))
    result.first.should(have.text("The DuckDB Local UI"))