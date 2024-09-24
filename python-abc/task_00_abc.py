#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class of an Animal"""

    @abstractmethod
    def sound(self,):
        """Abstract method
        Returns:
            str: the sound made by an animal"""
        pass


class Dog(Animal):
    """Subclass of Animal, represents a Dog"""
    def sound(self):
        """Returns the sound made by a dog"""
        return "Bark"


class Cat(Animal):
    """Subclass of Animal, represents a Cat"""
    def sound(self):
        """Returns the sound made by a cat"""
        return "Meow"
