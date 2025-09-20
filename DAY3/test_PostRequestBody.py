import pytest
import requests
import json

Student_id = None
request_headers = {"Content-Type": "application/json"}
BASE_URL = "http://localhost:3000/students"


# Dictionary

# def test_createStudentsPythonCustomClass():
#   global Student_id

# class Student:
#     def __init__(self, name, location, phone, courses):
#         self.name = name
#         self.location = location
#         self.phone = phone
#         self.courses = courses
#
# student = Student("Anjali", "Balkan", "12345678", ["Python", "Assembly"])
# request_body = student.__dict__
# response = requests.post(BASE_URL, json=request_body)
# # response = requests.post(BASE_URL, data=json.dumps(request_body), headers=request_headers)
#
# # assert if request is valid
# assert response.status_code == 201, "Status code is not 201"
# response_body = response.json()
# assert response_body["name"] == "Anjali", "Name is not correct"
# assert response_body["location"] == "Balkan", "Location is not correct"
# assert response_body["phone"] == "12345678", "Phone is not correct"
# assert response_body["courses"][0] == "Python", "Course 1 should be C"
# assert response_body["courses"][1] == "Assembly", "Course 2 should be C++"
# Student_id = response_body["id"]
# print(response.json())

# External File
def test_createStudentsExternalFile():
    global Student_id
    with open("DAY3/body.json", "r") as file:
        request_body = json.load(file)

    response = requests.post(BASE_URL, json=request_body)
    # response = requests.post(BASE_URL, data=json.dumps(request_body), headers=request_headers)

    # assert if request is valid
    assert response.status_code == 201, "Status code is not 201"
    response_body = response.json()
    assert response_body["name"] == "Anna Hathaway", "Name is not correct"
    assert response_body["location"] == "Washington", "Location is not correct"
    assert response_body["phone"] == "123466464", "Phone is not correct"
    assert response_body["courses"][0] == "C", "Course 1 should be C"
    assert response_body["courses"][1] == "C++", "Course 2 should be C++"
    Student_id = response_body["id"]
    print(response.json())


@pytest.fixture(autouse=True)
def delete_student():
    yield
    response = requests.delete(f"{BASE_URL}/{Student_id}")
    assert response.status_code == 200, "Status code is not 200"
    print(response.json())
    print("Student deleted")
