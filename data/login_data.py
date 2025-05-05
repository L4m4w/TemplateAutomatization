from dataclasses import dataclass
import random
import string

@dataclass
class User:
    username: str
    password: str


def random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_users(count=5):
    return [User(random_string(), random_string()) for _ in range(count)]