import json

import requests
import pytest

access_token = None #Global variable

@pytest.fixture(scope="session", autouse=True)
def generate_token():
    global access_token
    client_id = ""
    client_secret = ""
    token_url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    form_data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(token_url, data=form_data, headers=headers)
    assert response.status_code == 200, "Wrong status code"
    access_token = response.json()["access_token"]
    assert access_token is not None, "Wrong access token"

class TestOath2SpotifyAPI:
    def test_get_arijit_singh_top_tracks(self):
        response = requests.get("https://api.spotify.com/v1/artists/4YRxDV8wJFPHPTeXepOstw/top-tracks", headers={"Authorization": "Bearer " + access_token}, params={"market": "IN"})
        print("Status:", response.status_code)
        print("Response:", response.text)
        print("Access token:", access_token)
        assert response.status_code == 200, "Wrong status code"
        print(response.json())


