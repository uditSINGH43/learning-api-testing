import requests
import pytest
import json


class TestGraphQLQueries:
    BASE_URL = "https://hasura.io/learn/graphql"
    AUTH_TOKEN = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9FWTJSVGM1UlVOR05qSXhSRUV5TURJNFFUWXdNekZETWtReU1EQXdSVUV4UVVRM05EazFNQSJ9.eyJodHRwczovL2hhc3VyYS5pby9qd3QvY2xhaW1zIjp7IngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6InVzZXIiLCJ4LWhhc3VyYS1hbGxvd2VkLXJvbGVzIjpbInVzZXIiXSwieC1oYXN1cmEtdXNlci1pZCI6ImF1dGgwfDY4YzI5NTIzZjhiYTNiYjg3YzdlNjMzNCJ9LCJuaWNrbmFtZSI6IjIwMDR1ZGl0IiwibmFtZSI6IjIwMDR1ZGl0QGdtYWlsLmNvbSIsInBpY3R1cmUiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci84MGQ3MGYzYmMwNjViYjI1MDZmNmZmNzVlZjEzYWM3MT9zPTQ4MCZyPXBnJmQ9aHR0cHMlM0ElMkYlMkZjZG4uYXV0aDAuY29tJTJGYXZhdGFycyUyRjIwLnBuZyIsInVwZGF0ZWRfYXQiOiIyMDI1LTA5LTIzVDA3OjUwOjI5LjUyOFoiLCJpc3MiOiJodHRwczovL2dyYXBocWwtdHV0b3JpYWxzLmF1dGgwLmNvbS8iLCJhdWQiOiJQMzhxbkZvMWxGQVFKcnprdW4tLXdFenFsalZOR2NXVyIsInN1YiI6ImF1dGgwfDY4YzI5NTIzZjhiYTNiYjg3YzdlNjMzNCIsImlhdCI6MTc1ODYxMzgzMCwiZXhwIjoxNzU4NjQ5ODMwLCJzaWQiOiJNUnNpYXFjSEs1N0sxX3dXbTRDa0FYU3pudjYxT2lXUCIsImF0X2hhc2giOiJ4OFFmbmZiald5V25jOXI2WUhuSXJRIiwibm9uY2UiOiJGLi16Li5YY1YyUE5mSzZ5S3dYYlFHZEdUUXh3SHE2WCJ9.FRsPp-ML7rkfBz0DuZV1uLoYtW9P5WROnW5MwrWPXiR1EHX0eVqDRu-hv5M6pXB2_PXjxgSS1PmZY222ObmxXY_-_7d0tvTFTjYjV2MvA5-FjwSduL-K-BOu7kG0vUxuEqFFb71L-tgqu8Yh6JL0LtmvBtLH39SARElLYWLHWTihRxEvuq2rJaYGTXnQrU63ddIruzKjMHOkxbMioj21YQbP00Q58XMCKtnFzVel-tuV01W_FUJnlpl6bdfispWp1_sk2tCyqS44LWWDnMYOjHQGoC5QJoJKKJlKeYXL3UFSX9c-KfCaQn6adHNRLHL23nX-9StHhRnER5RCaHb0CA"
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": AUTH_TOKEN
    }

    # fetch users and their todos
    @pytest.mark.run(order=1)
    def test_fetch_users_their_todos(self):
        query = {
            "query": "query { users { name todos { title } } } "
        }

        res = requests.post(self.BASE_URL, headers=self.HEADERS, json=query)
        data = res.json()
        print("\nResposne\n", json.dumps(data, indent=4))
        assert "data" in data
        assert len(data["data"]["users"]) > 0
        assert data["data"]["users"][0]["name"] is not None
        assert isinstance(data["data"]["users"][0]["todos"], list)

    # fetch users and their todos
    @pytest.mark.run(order=2)
    def test_fetch_limited_todos(self):
        query = {
            "query": "query { todos(limit: 10) { id title } } "
        }

        res = requests.post(self.BASE_URL, headers=self.HEADERS, json=query)
        data = res.json()
        print("\nResposne\n", json.dumps(data, indent=4))
        assert "data" in data
        todos = data["data"]["todos"]
        assert len(todos) <= 10
        assert todos[0]['id'] is not None
        assert todos[0]['title'] is not None

    @pytest.mark.run(order=3)
    def test_fetch_users_with_recent_todos(self):
        query = {
            "query": "query { users(limit: 2) { id name todos(order_by: {created_at: desc}, limit: 5) { id title } } }"
        }

        res = requests.post(self.BASE_URL, headers=self.HEADERS, json=query)
        data = res.json()
        print("\nResposne\n", json.dumps(data, indent=4))
        assert "data" in data
        users = data["data"]["users"]
        assert len(users) == 2
        assert users[0]["name"] is not None
        assert isinstance(users[0]["todos"], list)

    @pytest.mark.run(order=4)
    def test_fetch_todos_with_variables(self):
        query = {
            "query": "query ($limit: Int!) { todos(limit: $limit) { id title } } ",
            "variables": {
                "limit": 10
            }
        }

        res = requests.post(self.BASE_URL, headers=self.HEADERS, json=query)
        data = res.json()
        print("\nResposne\n", json.dumps(data, indent=4))
        assert "data" in data
        todos = data["data"]["todos"]
        assert len(todos) <= 10
        assert todos[0]['id'] is not None
        assert todos[0]['title'] is not None

    @pytest.mark.run(order=5)
    def test_fetch_todos_with_where(self):
        query = {
            "query": "query { todos(where: {is_public: {_eq: true}}) { title is_public is_completed } }"
        }

        res = requests.post(self.BASE_URL, headers=self.HEADERS, json=query)
        data = res.json()
        print("\nResposne\n", json.dumps(data, indent=4))
        assert "data" in data
        todos = data["data"]["todos"]
        assert len(todos) > 0
        assert todos[0]["title"] is not None
        assert todos[0]["is_public"] is not None
        assert todos[0]["is_completed"] is not None
