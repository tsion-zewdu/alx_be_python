import math
from typing import Any


class Shape:

    def area(self) -> Any:
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):

    def __init__(self, length: float, width: float):
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise TypeError("length and width must be numbers")
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


__all__ = ["Shape", "Rectangle", "Circle"]

