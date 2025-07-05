import pytest
from selene import browser, by, be
from selenium import webdriver


@pytest.mark.parametrize("browser_management", [{"browsers": "Firefox", "device": "desktop"}], indirect=True)
def test_github_desktop(browser_management):
    browser.open('/')
    browser.element('[class="HeaderMenu-link HeaderMenu-link--sign-up HeaderMenu-button flex-shrink-0 d-flex d-lg-inline-flex no-underline border color-border-default rounded px-2 py-1"]').click()
    # s('').click()

@pytest.mark.parametrize("browser_management", [{"browsers": "Chrome", "device": "mobile"}], indirect=True)
def test_github_mobile(browser_management):
    browser.open('/')
    browser.element('[class="js-details-target js-nav-padding-recalculate js-header-menu-toggle Button--link Button--medium Button d-lg-none color-fg-inherit p-1"]').click()
    browser.element('[class="HeaderMenu-link HeaderMenu-link--sign-up HeaderMenu-button flex-shrink-0 d-flex d-lg-inline-flex no-underline border color-border-default rounded px-2 py-1"]').click()