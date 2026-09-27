import requests
import pytest

user_id = None #global variable

HEADERS = {
    "Content-Type": "application/json; charset=utf-8",
    "x-api-key": "reqres-free-v1"
}

@pytest.mark.order(1)
def test_get_users():
    res = requests.get("https://reqres.in/api/users?page=2", headers=HEADERS)
    print(res.json())
    assert res.status_code == 200, "Wrong status code"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 2, "Too slow"
    data = res.json()
    assert data.get("data") is not None, "Wrong data"
    print(data)
    assert data.get("page") == 2, "Wrong page"
    assert "email" in res.text, "Email not found"

@pytest.mark.dependency()
@pytest.mark.order(2)
def test_create_user():
    global user_id
    payload = {
        "name": "morpheus", "job": "leader"
    }
    res = requests.post("https://reqres.in/api/users", json=payload, headers=HEADERS)
    assert res.status_code == 201, "Wrong status code"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 2, "Too slow"
    data = res.json()
    assert data.get("name") == "morpheus", "Name mismatch"
    assert data.get("job") == "leader", "Job mismatch"
    assert "id" in data, "Missing id"
    user_id = data["id"]

@pytest.mark.order(3)
@pytest.mark.dependency(depends=["test_create_user"])
def test_update_user():
    payload = {"name": "heman", "job": "SDET"}
    res = requests.put(f"https://reqres.in/api/users/{user_id}", json=payload, headers=HEADERS)
    assert res.status_code == 200, "Wrong status code"
    assert res.headers["Content-Type"] == "application/json; charset=utf-8", "Wrong content type"
    assert res.elapsed.total_seconds() < 2, "Too slow"
    data = res.json()
    assert data.get("name") == "heman", "Name mismatch"
    assert data.get("job") == "SDET", "Job mismatch"
    assert "updatedAt" in data, "Missing Updated at"
    print(data)


@pytest.mark.order(4)
@pytest.mark.dependency(depends=["test_create_user"])
def test_delete_user():
    res = requests.delete(f"https://reqres.in/api/users/{user_id}", headers=HEADERS)
    assert res.status_code == 204, "Wrong status code"
    assert res.elapsed.total_seconds() < 2, "Too slow"
    assert res.text == "", "Response not empty"
    print("User deleted successfully")