import json

import pytest
import requests


@pytest.fixture(autouse=True)
def load_json_fixture(request):
    with open("./complex.json", "r") as file:
         request.cls.json_response = json.load(file)


class TestParseComplexJsonResponse:
    def test_user_details_validation(self):
        #verify status
        assert self.json_response["status"] == "success", "Wrong status code"

        #validate user details
        user_details = self.json_response["data"]["UserDetails"]
        assert user_details["id"] == 12345, "Wrong user id"
        assert user_details["name"] == "John Doe", "Wrong user name"
        assert user_details["email"] == "john.doe@example.com", "Wrong user email"

        #validation phone number and type
        phoneNumber = self.json_response["data"]["UserDetails"]["phoneNumbers"]
        assert phoneNumber[0]["type"] == "home", "Wrong phone number type"
        assert phoneNumber[0]["number"] == "123-456-7890", "Wrong phone number number"

        #validate Geo coordinates
        geo = user_details['address']["geo"]
        assert geo["latitude"] == 39.7817, "Wrong geo latitude"
        assert geo["longitude"] == -89.6501, "Wrong geo longitude"

        #validate preferences
        preferences = user_details["preferences"]
        assert preferences["notification"] == True, "Wrong preferences notification"
        assert preferences["theme"] == "dark", "Wrong preferences theme"





    def test_recent_orders_validation(self):
        recent_orders = self.json_response["data"]["recentOrders"]
        assert len(recent_orders)==2, "Wrong recent orders size"
        assert recent_orders[0]["orderId"]==101, "Wrong recent orders orderId"
        assert recent_orders[0]["totalAmount"] == 1226.49, "Wrong recent orders total amount"

        #verify second item name of item should be mouse
        assert recent_orders[0]["items"][1]["name"]=="Mouse", "Wrong recent orders items name"



    # def test_preferences_and_metadata_validation(self):

