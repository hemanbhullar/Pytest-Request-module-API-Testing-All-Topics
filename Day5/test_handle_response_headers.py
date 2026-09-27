import requests

class TestHeaders:
    def test_headers_in_response(self):
        url = "https://google.com"
        res = requests.get(url)
        assert res.status_code == 200, "Wrong status code"

        #capture all headers
        all_headers = res.headers
        print("All headers:", all_headers)

        #Extract Specific header
        print("Data header value:", all_headers["Date"])