
from pages.application import app

def test_workspace_change_name():
    app.workspace_home_page.open()
    app.workspace_home_page.edit_workspace_name_button.click()