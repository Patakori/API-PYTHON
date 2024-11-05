from .get_user_validator import get_user_validator

class MockRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_get_user_validator() -> None:
    request = MockRequest({
        "email": "dilsones@gmail.com"
    })

    get_user_validator(request)
