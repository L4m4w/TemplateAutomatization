import pytest

class TestLogin:
    @pytest.mark.platform("web")
    @pytest.mark.platform("mobile")
    def test_something(self):
        pass