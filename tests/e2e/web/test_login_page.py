from utils.utils_pages.utils_account import login_ui
from pages.application import app
from configs.settings import user_data

def test_create_repository():
    login_ui(user_data.email, user_data.password)
