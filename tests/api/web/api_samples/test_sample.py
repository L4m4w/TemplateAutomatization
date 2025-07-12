from dataclasses import dataclass
import pytest

# chrome_only = pytest.mark.parametrize("browser", ["Chrome"], indirect=True)

# @chrome_only
def test_chrome_extension():
    pass

@dataclass
class User:
    id: int
    name: str
    age: int
    description: str

    def __repr__(self):
        return f"{self.name} {self.age}"

user1 = User(id=1, name="Mario", age=32, description="something " * 10)

user2 = User(id=2, name="Wario", age=62, description="else " * 10)

def show_user(user):
    return f"{user.name} {user.age}"

@pytest.mark.parametrize("user", [user1, user2], ids=show_user)
def test_users(user):
    pass

@pytest.mark.parametrize("user", [user1, user2], ids=repr)
def test_users_repr(user):
    pass