import json
request_body = {
        "name": "Scott",
        "location": "France",
        "phone": "123456",
        "courses": ["C", "C++"]
}

print(type(request_body)) #<class 'dict'>
print(type(json.dumps(request_body))) #<class 'str'>
