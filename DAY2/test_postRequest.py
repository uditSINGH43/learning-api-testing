import requests
import json

Student_id = None
request_headers = {"Content-Type": "application/json"}
BASE_URL = "http://localhost:3000/students"
#Dictionary

def test_createStudents():
    request_body = {
        "name": "Elizabeth Olsen",
        "location": "America",
        "phone": "123466464",
        "courses": ["C", "C++"]
    }

    #response = requests.post(BASE_URL, json=request_body)
    response = requests.post(BASE_URL, data=json.dumps(request_body), headers=request_headers)

    #assert if request is valid
    assert response.status_code == 201, "Status code is not 201"
    response_body = response.json()
    assert response_body["name"] == "Elizabeth Olsen", "Name is not correct"
    assert response_body["location"] == "America", "Location is not correct"
    assert response_body["phone"] == "123466464", "Phone is not correct"
    assert response_body["courses"][0] == "C", "Course 1 should be C"
    assert response_body["courses"][1] == "C++", "Course 2 should be C++"
    Student_id = response_body["id"]
    print(response.json())