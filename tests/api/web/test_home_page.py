from selene import browser
from selenium import webdriver
from pages.application import app
from pages.workspace_home_page import WorkspaceHomePage

def test_workspace_change_name():
    app.workspace_home_page.open()
    app.workspace_home_page.edit_workspace_name_button.click()