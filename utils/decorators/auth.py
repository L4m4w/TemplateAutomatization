# utils/decorators/auth.py
from functools import wraps

from configs.settings import user_data
from utils.utils_pages.utils_account import get_auth_cookie


def with_auth_cookies(func):
    @wraps(func)
    def wrapper(browser_management, *args, **kwargs):
        cookies = get_auth_cookie(user_data.email, user_data.password)
        return func(browser_management, auth_cookies=cookies, *args, **kwargs)

    return wrapper