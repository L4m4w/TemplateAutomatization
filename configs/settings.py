from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings
from pathlib import Path

def find_project_root():
    current = Path(__file__).parent
    while not (current / ".git").exists() and not (current / "pyproject.toml").exists():
        if current.parent == current:
            return Path.cwd()
        current = current.parent
    return current

PROJECT_ROOT = find_project_root()

class UserData(BaseSettings):
    email : str = Field(..., alias="USER_DATA_EMAIL")
    password : str = Field(..., alias="USER_DATA_PASSWORD")
    username : str = Field(..., alias="USER_DATA_USERNAME")
    base_url : str = Field(..., alias="USER_DATA_BASE_URL")
    git_token : str = Field(..., alias="USER_DATA_GIT_TOKEN")
    token: str = Field(..., alias="USER_DATA_TOKEN")
    repository_name: str = Field(..., alias="USER_DATA_REPOSITORY_NAME")
    browserstack_username: str = Field(..., alias="USER_DATA_BROWSERSTACK_USERNAME")
    browserstack_access_key: str = Field(..., alias="USER_DATA_BROWSERSTACK_ACCESS_KEY")

    class Config:
        env_file = PROJECT_ROOT / ".env.local" if Path(".env.local").exists() else None
        env_prefix = "USER_DATA_"

class TestSettings(BaseSettings):
    base_url: str = "https://github.com/"
    headless: bool = True

user_data = UserData()
# settings = AISettings()
# test_settings = TestSettings()