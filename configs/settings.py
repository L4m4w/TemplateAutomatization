from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pathlib import Path

def find_project_root():
    current = Path(__file__).parent
    while not (current / ".git").exists() and not (current / "pyproject.toml").exists():
        if current.parent == current:
            return Path.cwd()  # Fallback
        current = current.parent
    return current

PROJECT_ROOT = find_project_root()

class UserData(BaseSettings):
    email : str
    password : str
    username : str
    base_url : str
    git_token : str
    token: str
    repository_name: str

    class Config:
        env_file = PROJECT_ROOT / ".env.local"
        env_prefix = "USER_DATA_"

class TestSettings(BaseSettings):
    base_url: str = "https://github.com/"
    headless: bool = True

user_data = UserData()
# settings = AISettings()
# test_settings = TestSettings()