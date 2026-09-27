import pytest
import requests
import json
from dataclasses import dataclass

student_id = None #Global Variable
Base_Url = "http://localhost:3000/students/"

requestHeader = {
    "Content-Type": "application/json",
}
# Dictionary
# def test_create_student_using_dictionary(delete_student):
#     global student_id
#     request_body = {
#         "name": "Delep2",
#         "location": "USA",
#         "phone": "123456",
#         "courses": ["C", "C++"]
#     }
#
#     res = requests.post(Base_Url, json=request_body)
#     # res = requests.post(Base_Url, data=json.dumps(request_body), headers=requestHeader)
#
#     assert res.status_code == 201, "Student creation failed"
#     response_body = res.json()
#     assert response_body["name"] == "Delep2", "Name is not created"
#     assert response_body["location"] == "USA", "Location is not created"
#     assert response_body["phone"] == "123456", "Phone is not created"
#     assert response_body["courses"] == ["C", "C++"], "Courses is not created"
#     student_id = response_body["id"]
#     print(student_id)
#     print(res.json())


@pytest.fixture()
def delete_student():
    yield
    res = requests.delete(f"{Base_Url}{student_id}")
    assert res.status_code == 200, "Student deletion failed"
    print(res.json())
    print("student deleted")



# * Json Module
# * Python custom class -- POJO class in java (Plain Old Java Object)

# def test_create_student_using_dictionary(delete_student):
#     global student_id
#
#     class Student:
#         def __init__(self, name, location, phone, courses):
#             self.name = name
#             self.location = location
#             self.phone = phone
#             self.courses = courses
#
#     student = Student("Delep2", "USA", "123456", ["C", "C++"]) #Object refrence variable
#     request_body = student.__dict__
#
#     res = requests.post(Base_Url, json=request_body)
#     # res = requests.post(Base_Url, data=json.dumps(request_body), headers=requestHeader)
#
#     assert res.status_code == 201, "Student creation failed"
#     response_body = res.json()
#     assert response_body["name"] == "Delep2", "Name is not created"
#     assert response_body["location"] == "USA", "Location is not created"
#     assert response_body["phone"] == "123456", "Phone is not created"
#     assert response_body["courses"] == ["C", "C++"], "Courses is not created"
#     student_id = response_body["id"]
#     print(student_id)
#     print(res.json())


# * dataclass -> similar to custom classes but this is only for holding the data

# def test_create_student_using_dictionary(delete_student):
#     global student_id
#
#     @dataclass
#     class Student:
#         name:str
#         location:str
#         phone:str
#         courses:list
#
#
#     student = Student("Delep2", "USA", "123456", ["C", "C++"]) #Object refrence variable
#     request_body = student.__dict__
#
#     res = requests.post(Base_Url, json=request_body)
#     # res = requests.post(Base_Url, data=json.dumps(request_body), headers=requestHeader)
#
#     assert res.status_code == 201, "Student creation failed"
#     response_body = res.json()
#     assert response_body["name"] == "Delep2", "Name is not created"
#     assert response_body["location"] == "USA", "Location is not created"
#     assert response_body["phone"] == "123456", "Phone is not created"
#     assert response_body["courses"] == ["C", "C++"], "Courses is not created"
#     student_id = response_body["id"]
#     print(student_id)
#     print(res.json())

# * Sometimes we are using. -> External json file

def test_create_student_using_external_file(delete_student):
    global student_id

    with open("./Day3/body.json", 'r') as file:
        request_body = json.load(file)

    res = requests.post(Base_Url, json=request_body)
    # res = requests.post(Base_Url, data=json.dumps(request_body), headers=requestHeader)

    assert res.status_code == 201, "Student creation failed"
    response_body = res.json()
    assert response_body["name"] == "Scott", "Name is not created"
    assert response_body["location"] == "France", "Location is not created"
    assert response_body["phone"] == "343234322", "Phone is not created"
    assert response_body["courses"] == ["C", "C++"], "Courses is not created"
    student_id = response_body["id"]
    print(student_id)
    print(res.json())
