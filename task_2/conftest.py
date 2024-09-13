import pytest
import requests
from http import HTTPMethod
from configuration import BASE_URL, API
from constant import BODY


@pytest.fixture()
def save():
    response = requests.request(
        HTTPMethod.POST,
        f"{BASE_URL}{API}",
        json=BODY,
    )
    return response
