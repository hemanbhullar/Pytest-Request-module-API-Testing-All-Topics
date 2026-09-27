import json

import requests

access_token = None #Global variable

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
    print(response.json())


generate_token()
