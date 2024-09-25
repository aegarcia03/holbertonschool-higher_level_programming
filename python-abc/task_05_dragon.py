#!/usr/bin/env python3


class SwimMixin:
    """SwimMixin class"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """FlyMixin class"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits from SwimMixin and FlyMixin"""
    def roar(self):
        print("The dragon roars!")
