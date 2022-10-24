#!/usr/bin/python3

class BaseGeometry():
    """Base geometry class"""
    def area(self):
        """When area is not implemented"""
        raise Exception("area() is not implented")
