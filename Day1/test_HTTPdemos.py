import requests
import pytest


HEADERS = {'Content-Type': 'application/json',
           "x-api-key": "reqres-free-v1"
}

def test_get_users():
    req = requests.get("https://reqres.in/api/users?page=2",headers=HEADERS)
    print(req.json())
    assert req.status_code == 200, "Wrong status"
    data = req.json()
    assert data.get("page") == 2, "Wrong page"
