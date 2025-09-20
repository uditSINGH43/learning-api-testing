import json

# request_body = {
#         "name": "Elizabeth Olsen",
#         "location": "America",
#         "phone": "123466464",
#         "courses": ["C", "C++"]
# }
#
# print(type(request_body)) #class dict
# print(type(json.dumps(request_body))) #class str



# class Student:
#     def __init__(self, name, location, phone, courses):
#         self.name = name
#         self.location = location
#         self.phone = phone
#         self.courses = courses
#
#
# student = Student("Anjali", "Balkan", "12345678", ["Python", "Assembly"])
# print(student.__dict__)

from dataclasses import dataclass
@dataclass
class Student:
    name:str
    location:str
    phone:str
    courses:list

student = Student("Anjali", "Balkan", "12345678", ["Python", "Assembly"])
print(student.__dict__)
print(type(student.__dict__))