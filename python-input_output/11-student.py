#!/usr/bin/python3

"""class"""


class Student:
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            attributes = {}
            for attr in attrs:
                if isinstance(attr, str) and attr in self.__dict__:
                    attributes[attr] = self.__dict__[attr]
            return attributes
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
