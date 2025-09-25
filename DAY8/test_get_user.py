import json

import requests

BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = "be43dc37c2123910441d0306d8ee84611057592a1d67651a2358b7440252a690"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


class TestGetUser:
    def test_get_user_details(self, create_user):
        user_id = create_user
        assert user_id is not None, "User ID not set by create user test"
        res = requests.get(f"{BASE_URL}/{user_id}", headers=HEADERS)
        assert res.status_code == 200, "Details fetch failed"
        print("\nGET Response\n", json.dumps(res.json(), indent=4))
