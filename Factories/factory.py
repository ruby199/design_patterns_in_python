"""
Factory 
- [DEF] A component responsible solely for the wholesale (not piecewise) creation of objects.


The Factory Design Pattern is a creational pattern used in Object-Oriented Programming (OOP) to encapsulate the process of creating objects. The core idea of this pattern is to use a separate class to create instances of other classes, thereby abstracting the instantiation process. This pattern is particularly useful when the exact type of the objects to be created is determined at runtime.
"""
from enum import Enum
from math import *

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    # def __init__(self, x, y):
    #     self.x = x
    #     self.y = y

    # redeclaration won't work
    # def __init__(self, rho, theta):
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
    
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)

        # steps to add a new system
        # 1. augment CoordinateSystem
        # 2. change init method
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))

    class Factory:
        @staticmethod
        def new_cartesian_point(x, y):
            return Point(x, y)
    
    factory = Factory()


# take out factory methods to a separate class
class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))


if __name__ == '__main__':
    p1 = Point(2, 3, CoordinateSystem.CARTESIAN)
    p2 = PointFactory.new_cartesian_point(1, 2)
    # or you can expose factory through the type
    p3 = Point.Factory.new_cartesian_point(5, 6)
    p4 = Point.factory.new_cartesian_point(7, 8)
    print(p1, p2, p3, p4)

