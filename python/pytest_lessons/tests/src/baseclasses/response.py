from typing import Iterable
from jsonschema import validate

class Response:
    def __init__(self, response):
        self.response = response 

    def validate(self, schema):
        if isinstance(schema, Iterable):
            for item in self.response: 
                validate(item, schema)
        else:
            validate(self.response, schema)