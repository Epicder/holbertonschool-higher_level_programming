#!/usr/bin/python3


"""create a class"""


class BaseGeometry:
    """class"""
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        """class"""


class Rectangle(BaseGeometry):
    """new class"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)

    def area(self):
        area = self.__width * self.__height
        return area

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """class"""
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        area = self.__size * self.__size
        return area

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
