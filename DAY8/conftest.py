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


@pytest.fixture(scope="session", autouse=True)
def create_user():
    faker = Faker()
    data = {
        "name": faker.name(),
        "gender": "Female",
        "email": faker.unique.email(),
        "status": "inactive",
    }
    response = requests.post(BASE_URL, json=data, headers=HEADERS)
    assert response.status_code == 201, "Wrong status code"
    print("\nCREATE Response\n", json.dumps(response.json(), indent=4))
    return response.json()["id"]
