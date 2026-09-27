import pytest
import requests
import json
from faker import Faker

BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = "63fe5edb6fcda1d221073e81c2579f48f1304040c37e37eb267c8a028ef56e85"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

@pytest.fixture(scope="session", autouse=True)
def create_user():
    faker = Faker()
    data = {
        "name": faker.name(),
        "gender": "Male",
        "email": faker.unique.email(),
        "status": "inactive"
    }

    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    assert response.status_code == 201, "Wrong status code"
    user_id = response.json()["id"]
    assert user_id, "User id is not generated"
    print("\nCreate Response\n", json.dumps(response.json(), indent=4))
    return user_id
