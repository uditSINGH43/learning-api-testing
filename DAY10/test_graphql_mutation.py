import requests
import pytest
import json


class TestGraphQLMutations:
    BASE_URL = "https://hasura.io/learn/graphql"
    AUTH_TOKEN = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9FWTJSVGM1UlVOR05qSXhSRUV5TURJNFFUWXdNekZETWtReU1EQXdSVUV4UVVRM05EazFNQSJ9.eyJodHRwczovL2hhc3VyYS5pby9qd3QvY2xhaW1zIjp7IngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6InVzZXIiLCJ4LWhhc3VyYS1hbGxvd2VkLXJvbGVzIjpbInVzZXIiXSwieC1oYXN1cmEtdXNlci1pZCI6ImF1dGgwfDY4YzI5NTIzZjhiYTNiYjg3YzdlNjMzNCJ9LCJuaWNrbmFtZSI6IjIwMDR1ZGl0IiwibmFtZSI6IjIwMDR1ZGl0QGdtYWlsLmNvbSIsInBpY3R1cmUiOiJodHRwczovL3MuZ3JhdmF0YXIuY29tL2F2YXRhci84MGQ3MGYzYmMwNjViYjI1MDZmNmZmNzVlZjEzYWM3MT9zPTQ4MCZyPXBnJmQ9aHR0cHMlM0ElMkYlMkZjZG4uYXV0aDAuY29tJTJGYXZhdGFycyUyRjIwLnBuZyIsInVwZGF0ZWRfYXQiOiIyMDI1LTA5LTIzVDA3OjUwOjI5LjUyOFoiLCJpc3MiOiJodHRwczovL2dyYXBocWwtdHV0b3JpYWxzLmF1dGgwLmNvbS8iLCJhdWQiOiJQMzhxbkZvMWxGQVFKcnprdW4tLXdFenFsalZOR2NXVyIsInN1YiI6ImF1dGgwfDY4YzI5NTIzZjhiYTNiYjg3YzdlNjMzNCIsImlhdCI6MTc1ODYxMzgzMCwiZXhwIjoxNzU4NjQ5ODMwLCJzaWQiOiJNUnNpYXFjSEs1N0sxX3dXbTRDa0FYU3pudjYxT2lXUCIsImF0X2hhc2giOiJ4OFFmbmZiald5V25jOXI2WUhuSXJRIiwibm9uY2UiOiJGLi16Li5YY1YyUE5mSzZ5S3dYYlFHZEdUUXh3SHE2WCJ9.FRsPp-ML7rkfBz0DuZV1uLoYtW9P5WROnW5MwrWPXiR1EHX0eVqDRu-hv5M6pXB2_PXjxgSS1PmZY222ObmxXY_-_7d0tvTFTjYjV2MvA5-FjwSduL-K-BOu7kG0vUxuEqFFb71L-tgqu8Yh6JL0LtmvBtLH39SARElLYWLHWTihRxEvuq2rJaYGTXnQrU63ddIruzKjMHOkxbMioj21YQbP00Q58XMCKtnFzVel-tuV01W_FUJnlpl6bdfispWp1_sk2tCyqS44LWWDnMYOjHQGoC5QJoJKKJlKeYXL3UFSX9c-KfCaQn6adHNRLHL23nX-9StHhRnER5RCaHb0CA"

    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": AUTH_TOKEN
    }
    inserted_todo_id = None

    @pytest.mark.run(order=1)
    def test_insert_todo(self):
        query = {
            "query": "mutation { insert_todos(objects: [{title: \"sdet QA 123\"}]) { affected_rows returning { id created_at title } } }"
        }

        res = requests.post(self.BASE_URL, headers=self.HEADERS, json=query)
        data = res.json()
        print("\nResposne\n", json.dumps(data, indent=4))
        assert "data" in data
        todo = data["data"]["insert_todos"]["returning"][0]
        self.__class__.inserted_todo_id = todo["id"]
        assert todo["title"] == "sdet QA 123"

    @pytest.mark.run(order=2)
    def test_update_todo(self):
        update_mutation = {
            "query": f"""
                      mutation {{
                        update_todos(
                          where: {{id: {{_eq: {self.inserted_todo_id}}}}},
                          _set: {{title: "sdetqa", is_completed: true}}
                        ) {{
                          affected_rows
                          returning {{
                            id
                            title
                            is_completed
                          }}
                        }}
                      }}
                  """
        }
        res = requests.post(self.BASE_URL, headers=self.HEADERS, json=update_mutation)
        data = res.json()
        print("\nResposne\n", json.dumps(data, indent=4))
        assert "data" in data

    @pytest.mark.run(order=3)
    def test_delete_todo(self):
        delete_mutation = {
            "query": f"""
                       mutation {{
                         delete_todos(where: {{id: {{_eq: {self.inserted_todo_id}}}}}) {{
                           affected_rows
                           returning {{
                             title
                           }}
                         }}
                       }}
                   """
        }
        res = requests.post(self.BASE_URL, headers=self.HEADERS, json=delete_mutation)
        data = res.json()
        print("\nResposne\n", json.dumps(data, indent=4))
        assert "data" in data
