#!/usr/bin/python3

import pickle


class CustomObject:
    name = ""
    age = None
    is_student = None

    def __init__(self, name="Jhon", age=25, is_student=True):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as pfile:
                pickle.dump(self, pfile)
        except Exception as e:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as pfile:
                code = pickle.load(pfile)
                return code
        except Exception as e:
            return None
