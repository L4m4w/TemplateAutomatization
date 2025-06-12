from selene import browser, be, have

from configs.settings import user_data
from pages.application import app

from utils.utils_pages.utils_account import get_auth_cookie

def test_create_new_branch():
    cookies = get_auth_cookie(user_data.email, user_data.password)

    app.branch_page.with_cookies(cookies).open()

    app.branch_page.create_new_branch()
    browser.element("div[title='321']").with_(timeout=10).should(be.visible)

def test_branch_name_already_exist():
    cookies = get_auth_cookie(user_data.email, user_data.password)
    app.branch_page.with_cookies(cookies).open()
    app.branch_page.create_new_branch()
    app.branch_page.error_message_box.should(have.text('Sorry, that branch already exists.'))

def test_branch_in_branch_table():
    cookies = get_auth_cookie(user_data.email, user_data.password)
    app.branch_page.with_cookies(cookies).open()
    # app.branch_page.get_user_branch_from_table('321')
    branch = app.branch_page.get_user_branch_from_table()
    branch_link = branch.element('..')
    print(debug_element(branch_link))
    # branch_link = branch_link.element('//a')
    # branch_link = app.branch_page.branch_href_link('321')
    # all_attributes = browser.driver.execute_script(
    #     """
    #     const elem = arguments[0];
    #     const attributes = {};
    #     for (let i = 0; i < elem.attributes.length; i++) {
    #         attributes[elem.attributes[i].name] = elem.attributes[i].value;
    #     }
    #     return attributes;
    #     """,
    #     branch_link.locate()  # Получаем Selenium-WebElement
    # )
    # print(all_attributes)
    # print(branch_link.)
    # branch_link.should(have.css_property('href', "/evgne/Desiree-Leblanc/tree/321"))
    # href = branch_link.should(have.attribute("href"))
    # branch_link.should(have.attribute('href', "/evgne/Desiree-Leblanc/tree/321"))

from selene import command

def debug_element(element):
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