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
        if attrs == None:
            return self.__dict__
        if isinstance(attrs, list):
            attributes = {}
            for attr in attrs:
                if isinstance(attr, str) and attr in self.__dict__:
                    attributes[attr] = self.__dict__[attr]
            return attributes
        return self.__dict__
