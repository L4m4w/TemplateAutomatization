from selene import browser
from selene.core.entity import Element
from selenium.webdriver.remote.webelement import WebElement


def debug_element(element: Element):
    return browser.driver.execute_script(
        """
        const elem = arguments[0];
        return {
            attributes: Array.from(elem.attributes).reduce((acc, attr) => {
                acc[attr.name] = attr.value;
                return acc;
            }, {}),
            css: Array.from(window.getComputedStyle(elem)).reduce((acc, key) => {
                acc[key] = styles.getPropertyValue(key);
                return acc;
            }, {}),
            text: elem.textContent,
            rect: elem.getBoundingClientRect().toJSON(),
        };
        """,
        element.locate()
    )

def debug_get_css_attributes(element: Element):
    all_attributes = browser.driver.execute_script(
        """
        const elem = arguments[0];
        const attributes = {};
        for (let i = 0; i < elem.attributes.length; i++) {
            attributes[elem.attributes[i].name] = elem.attributes[i].value;
        }
        return attributes;
        """,
        element.locate()
    )
    return all_attributes