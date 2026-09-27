import requests

class TestCookies:

    def test_cookies_in_response(self):
        url = "https://google.com"
        res = requests.get(url)
        assert res.status_code == 200, "Wrong status code"
        all_cookies = res.cookies
        print("All Cookies: ", all_cookies)

        #Assert cookie and check if it is not none
        assert "AEC" in all_cookies, "AEC cookie not in response"
        assert all_cookies.get("AEC") is not None, "AEC cookie is None"

        #Extract a specific cookie
        cookie_value = all_cookies.get("AEC")
        print("Cookie value: ", cookie_value)

        #Iterate through each and every cookie and print
        for key, value in all_cookies.items():
            print(f"{key}: {value}")