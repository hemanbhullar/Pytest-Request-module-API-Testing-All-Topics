import requests
import json

student_id = None #Global Variable
Base_Url = "http://localhost:3000/students/"

requestHeader = {
    "Content-Type": "application/json",
}
# Dictionary
def test_create_student_using_dictionary():
    request_body = {
        "name": "Scott",
        "location": "France",
        "phone": "123456",
        "courses": ["C", "C++"]
    }

    # res = requests.post(Base_Url, json=request_body)
    res = requests.post(Base_Url, data=json.dumps(request_body), headers=requestHeader)

    assert res.status_code == 201, "Student creation failed"
    response_body = res.json()
    assert response_body["name"] == "Scott", "Name is not created"
    assert response_body["location"] == "France", "Location is not created"
    assert response_body["phone"] == "123456", "Phone is not created"
    assert response_body["courses"] == ["C", "C++"], "Courses is not created"
    student_id = response_body["id"]
    print(res.json())



# * Json Module
# * Python custom class -- POJO class in java (Plain Old Java Object)
# * dataclass -> similar to custom classes but this is only for holding the data
# * Sometimes we are using. -> External json file
