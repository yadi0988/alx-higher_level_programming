#!/usr/bin/python3
"class Rectangle that inherits from Base"
from models.base import Base


class Rectangle(Base):
    "class Rectangle that inherits from Base"
    def __init__(self, width, height, x=0, y=0, id=None):
        self.validation("width", width)
        self.width = width
        self.validation("height", height)
        self.height = height
        self.validation("x", x)
        self.x = x
        self.validation("y", y)
        self.y = y
        super().__init__(id)

    def validation(self, name, value):
        "............."
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(name + " must be >= 0")

        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(name + " must be > 0")

    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.validation("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.validation("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.validation("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.validation("y", y)
        self.__y = y
