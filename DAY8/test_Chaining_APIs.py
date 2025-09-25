import requests
import json
import pytest
from faker import Faker

BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = "be43dc37c2123910441d0306d8ee84611057592a1d67651a2358b7440252a690"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
faker = Faker()


class TestChainingAPIs:
    user_id = None  # class Variable

    @pytest.mark.dependency(name="Create")
    def test_get_user(self):
        data = {
            "name": faker.name(),
            "gender": "Female",
            "email": faker.unique.email(),
            "status": "inactive",
        }
        res = requests.post(BASE_URL, json=data, headers=HEADERS)

        assert res.status_code == 201, "Wrong status code"
        TestChainingAPIs.user_id = res.json()["id"]
        assert TestChainingAPIs.user_id, "UserID did not generate"
        print("\nCREATE Response\n", json.dumps(res.json(), indent=4))

    @pytest.mark.dependency(depends=["Create"])
    def test_get_user_details(self):
        res = requests.get(f"{BASE_URL}/{TestChainingAPIs.user_id}", headers=HEADERS)
        assert res.status_code == 200, "Wrong status code"
        print("\nGET Response\n", json.dumps(res.json(), indent=4))

    @pytest.mark.dependency(depends=["Create"])
    def test_Update_user(self):
        updated_data = {
            "name": faker.name(),
            "gender": "male",
            "email": faker.unique.email(),
            "status": "active",
        }
        res = requests.put(f"{BASE_URL}/{TestChainingAPIs.user_id}", json=updated_data, headers=HEADERS)

        assert res.status_code == 200, "Wrong status code"
        print("\nUPDATE Response\n", json.dumps(res.json(), indent=4))

    @pytest.mark.dependency(depends=["Create"])
    def test_Delete_user(self):
        res = requests.delete(f"{BASE_URL}/{TestChainingAPIs.user_id}", headers=HEADERS)

        assert res.status_code == 204, "Wrong status code"
