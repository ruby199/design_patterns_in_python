
"""
# LSP: Liskov Substitution Principle
- Objects in a program should be replaceable with instances of their subtypes without altering the correctness of the program.

In simpler terms, if class B is a subtype of class A, then we should be able to replace A with B without disrupting the behavior of our program. This principle aims to ensure that a subclass or derived class should extend the base or parent class without changing its behavior.In simpler terms, if class B is a subtype of class A, then we should be able to replace A with B without disrupting the behavior of our program. This principle aims to ensure that a subclass or derived class should extend the base or parent class without changing its behavior.


"""

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

"""
Consider a class Rectangle with methods setWidth and setHeight. 
If you derive a class Square from Rectangle, it might be tempting to override these methods in Square so that both the height and width are set to the same value. 

However, this would violate LSP, because changing the width of a Square would unexpectedly change its height, which is not the behavior of a Rectangle.
"""
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
