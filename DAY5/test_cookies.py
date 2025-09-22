import requests


class TestCookies:
    def test_cookiesResponse(self):
        url = "http://www.google.com"
        req = requests.get(url)
        assert req.status_code == 200, "Wrong status code"

        # capture all cookies
        all_cookies = req.cookies
        print("All Cookies:", all_cookies)

        # asserting cookies
        assert "AEC" in all_cookies, "not found"
        assert all_cookies.get("AEC") is not None, "AEC not found"

        # Extarcting a specific cookie
        cookie_value = all_cookies.get("AEC")
        print("Cookie_Value:", cookie_value)

        # Iterate through each and every cookie and print
        for key, value in all_cookies.items():
            print(f"{key}: {value}")
