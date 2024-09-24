#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class of a Shape"""

    @abstractmethod
    def area(self,):
        """Abstract method
        Returns:
            area: the area of a shape"""
        pass

    @abstractmethod
    def perimeter(self,):
        """Abstract method
        Returns:
            perimeter: the perimeter of a shape"""
        pass


class Circle(Shape):
    """Subclass of Shape, represents a Circle"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Returns the area of a Circle"""
        return math.pi * (self.radius * self.radius)

    def perimeter(self):
        """Return the perimeter of a Circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Subclass of Shape, represents a Rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of a Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a Rectangle"""
        return 2 * (self.height + self.width)


def shape_info(shape):
    """Prints the area and perimeter of the shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
