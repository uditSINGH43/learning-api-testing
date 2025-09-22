import requests

class TestHeaders:
    def test_headers_in_response(self):
        url = "http://www.google.com"
        req = requests.get(url)
        assert req.status_code == 200, "Wrong status code"

        #capture all headers
        all_headers = req.headers
        print("All Headers", all_headers)

        #extract a  specific header
        print("Date Header Value", all_headers["Date"])