from configs.settings import user_data
from pages.application import app

from utils.utils_pages.utils_account import get_auth_cookie

def test_1():
    cookie = get_auth_cookie(user_data.email, user_data.password)
    print(cookie)
    app.
