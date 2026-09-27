import pytest
import requests
import json
from faker import Faker

@pytest.fixture(scope="session", autouse=True)
def get_token():
    faker = Faker()
    payload = {
        "clientName": "kmr",
        "clientEmail": faker.email()
    }
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=payload, headers=headers)

    print(response.status_code)
    print(response.text)
    return response.json().get("accessToken")