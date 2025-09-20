import requests

from Day1.test_HTTPdemos import HEADERS


def test_pathparam():
    country = "India"
    response = requests.get(f"https://restcountries.com/v2/name/{country}")
    assert response.status_code == 200
    print(response.json())


def test_QueryParam():
    queryParams = {"page": 2}
    HEADERS = {
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }
    res = requests.get("https://reqres.in/api/users", params=queryParams, headers=HEADERS)
    print(res.status_code)
    print(res.json())
