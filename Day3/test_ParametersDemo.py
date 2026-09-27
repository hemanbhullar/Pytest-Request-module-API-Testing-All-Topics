import requests
HEADERS = {"Content-Type": "application/json"}

def test_path_parameters():
    country = "Canada"
    response = requests.get(f"https://reqres.in/api/users?country={country}", headers=HEADERS)
    assert response.status_code == 200
    print(response.json())



def test_query_parameters():
    query_params = {"page": "2"}
    res = requests.get("https://reqres.in/api/users",params=query_params, headers=HEADERS)
    print(res.status_code)
    print(res.json())