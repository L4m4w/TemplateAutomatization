from selene import browser, Config
from selenium.webdriver import ChromeOptions

def setup_browser():
    options = ChromeOptions()
    options.add_argument("--headless")  # Для CI
    browser.set_driver(Config(
        driver_options=options,
        timeout=10,
        base_url="https://demoqa.com"  # Пример базового URL
    ))