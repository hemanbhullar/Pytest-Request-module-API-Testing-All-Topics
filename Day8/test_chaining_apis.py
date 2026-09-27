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
faker = Faker()

class TestChainingAPIs:
    user_id = None #class variable

    @pytest.mark.dependency(name="create")
    def test_create_user(self):
        data = {
            "name": faker.name(),
            "gender": "Male",
            "email": faker.unique.email(),
            "status": "inactive"
        }

        response = requests.post(BASE_URL, json=data, headers=HEADERS)
        assert response.status_code == 201, "Wrong status code"
        TestChainingAPIs.user_id = response.json()["id"]
        assert TestChainingAPIs.user_id, "User id is not generated"
        print("\nCreate Response\n", json.dumps(response.json(), indent=4))

    @pytest.mark.dependency(depends=["create"])
    def test_get_user_details(self):
        print(TestChainingAPIs.user_id)
        response = requests.get(f"{BASE_URL}/{TestChainingAPIs.user_id}/", headers=HEADERS)
        assert response.status_code == 200, "Wrong status code"

    @pytest.mark.dependency(depends=["create"])
    def test_update_user(self):
        data = {
            "name": faker.name(),
            "gender": "Male",
            "email": faker.unique.email(),
            "status": "active"
        }

        response = requests.put(f"{BASE_URL}/{TestChainingAPIs.user_id}", json=data, headers=HEADERS)
        assert response.status_code == 200, "Wrong status code"
        print("\nUpdate Response\n", json.dumps(response.json(), indent=4))

    @pytest.mark.dependency(depends=["create"])
    def test_delete_user_details(self):
        print(TestChainingAPIs.user_id)
        response = requests.delete(f"{BASE_URL}/{TestChainingAPIs.user_id}/", headers=HEADERS)
        assert response.status_code == 204, "Wrong status code"
