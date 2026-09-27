import requests
import json
import pytest

from Day9.test_data_providers import read_csv_data
from test_data_providers import read_json_data

BASE_URL = "https://simple-books-api.glitch.me/orders"


def submit_delete_order(bookid, customer_name, get_token):
    print("get token", get_token)
    headers = {
        "Authorization": f"Bearer {get_token}",
        "Content-Type": "application/json"
    }

    print("headers request", headers)

    payload = {
        "bookId": int(bookid),
        "customerName": customer_name
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)
    print(json.dumps(response.json(), indent=4))
    print("headers", response.request.headers)
    print(response.status_code)
    assert response.status_code == 201

@pytest.mark.parametrize('order_data', read_json_data('./TestData/orders_json_data.json'))
def test_with_json_data(order_data,get_token):
    order_data = order_data[0]
    submit_delete_order(order_data["BookID"], order_data["CustomerName"], get_token)


@pytest.mark.parametrize('book_id,customer_name', read_csv_data('./TestData/orders_csv_data.csv'))
def test_with_csv_data(book_id, customer_name,get_token):
    submit_delete_order(book_id, customer_name, get_token)


