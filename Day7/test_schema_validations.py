import requests
import json
import xmlschema
from jsonschema import validate, ValidationError

class TestSchemaValidations:
    def test_json_schema_validation(self):
        url = "https://mocktarget.apigee.net/json"
        res = requests.get(url)
        print(res.json())
        assert res.status_code == 200

        #load schema and response
        data =res.json()
        with open("./JSONSchema.json", 'r') as f:
            schema = json.loads(f.read())

        try:
            validate(instance=data, schema=schema)
            print("JSON Schema is validation passed")
        except ValidationError as e:
            print("JSON Schema is validation failed")
            print(e)
            assert False


    def test_xml_schema_validation(self):
        url = "https://mocktarget.apigee.net/xml"
        res = requests.get(url)
        assert res.status_code == 200
        #load XML schema
        schema = xmlschema.XMLSchema("./XMLSchema.xsd")

        try:
            schema.validate(res.text)
            print("XML Schema is validation passed")
        except ValidationError as e:
            print("XML Schema is validation failed")
            print(e)
            assert False