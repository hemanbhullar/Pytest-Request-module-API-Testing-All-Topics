import requests, json

BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = "63fe5edb6fcda1d221073e81c2579f48f1304040c37e37eb267c8a028ef56e85"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

class TestGetUser:
    def test_get_user_details(self, create_user):
        user_id = create_user
        print(user_id)
        response = requests.get(f"{BASE_URL}/{user_id}/", headers=HEADERS)
        assert response.status_code == 200, "Wrong status code"
        print("\n Get User Details \n", json.dumps(response.json(), indent=4))
