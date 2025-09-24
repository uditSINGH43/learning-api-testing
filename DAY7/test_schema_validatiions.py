import requests
import xmlschema
import json
from jsonschema import validate, ValidationError


class TestSchemaValidation:
    def test_json_schema_validation(self):
        url = 'https://mocktarget.apigee.net/json'
        res = requests.get(url)
        assert res.status_code == 200

        # Load Schema and Response
        data = res.json()
        with open("DAY7/Jsonschema.json", "r") as f:
            schema = json.load(f)
        try:
            validate(instance=data, schema=schema)
            print("JSON Schema validation passed")
        except ValidationError as e:
            print("JSON Schema validation Failed: ", e)
            assert False

    def test_xml_schema_validation(self):
        url = 'https://mocktarget.apigee.net/xml'
        res = requests.get(url)
        assert res.status_code == 200

        # Load XML Schema
        schema = xmlschema.XMLSchema("./xmlschema.xsd")

        try:
            schema.validate(res.text)
            print("XML Schema validation passed")
        except:
            print("XML Schema validation failed")
            assert False
