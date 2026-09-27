import requests
import json

class TestOrderAPI:
    BASE_URL = "https://simple-books-api.glitch.me/orders"

    def test_submit_delete_order(self, get_token):
        print("get token", get_token)
        headers = {
            "Authorization": f"Bearer {get_token}",
            "Content-Type": "application/json"
        }

        print("headers request", headers)

        payload = {
            "bookId": 1,
            "customerName": "JAM"
        }

        response = requests.post(self.BASE_URL, headers=headers, json=payload)
        print(json.dumps(response.json(), indent=4))
        print("headers",response.request.headers)
        print(response.status_code)
        assert response.status_code == 201

