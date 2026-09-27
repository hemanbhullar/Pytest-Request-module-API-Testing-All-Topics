import requests
from requests.auth import HTTPDigestAuth

class TestAuthentication:
    def test_basic_auth(self):
        res = requests.get("https://postman-echo.com/basic-auth", auth=("postman", "password"))
        assert res.status_code == 200 , "Wrong status code"
        print(res.json())
        assert res.json().get("authenticated") is True , "Authentication failed"

    def test_digest_auth(self):
        res = requests.get("https://postman-echo.com/digest-auth", auth=HTTPDigestAuth("postman", "password"))
        assert res.status_code == 200, "Wrong status code"
        print(res.json())
        assert res.json().get("authenticated") is True, "Authentication failed"

    def test_bearer_token_auth(self):
        bearer_token = ""
        headers = {"Authorization": f"Bearer {bearer_token}"}
        response = requests.get("https://api.github.com/user/repos", headers=headers)
        assert response.status_code == 200, "Wrong status code"
        print(response.json())

    def test_api_key_auth(self):
        params= {
            "q": "Chennai",
            "appid": "1ab7436048d1568c74fd5394cb0ffd17"
        }

        response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        print("URL:", response.url)
        print("Status:", response.status_code)
        print("Response:", response.text)
        assert response.status_code == 200, "Wrong status code"
        print(response.json())

