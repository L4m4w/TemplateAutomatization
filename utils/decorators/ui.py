from selene import browser

def screenshot_on_failure(func):
    """
    Decorator for automatic screenshot on test failure
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            browser.driver.save_screenshot(f"fail_{func.__name__}.png")
            raise
    return wrapper