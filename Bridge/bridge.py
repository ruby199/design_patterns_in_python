"""
Bridge Design Pattern:

[DEF]: A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
    - Decouple abstraction from implementation
    - Both can exist as hierarchies
    - A stronger form of encapsulation

[Motivation]
    - Bridge prevents a 'Cartesian product' complexity explosion.

[Advantages]:
    1. Bridge pattern decouple an abstraction from its implementation so that the two can vary independently.

    2. It is used mainly for implementing platform independence features.

    3. It adds one more method level redirection to achieve the objective.

    4. Publish abstraction interface in a separate inheritance hierarchy, and put the implementation in its own inheritance hierarchy.

    5. Use bridge pattern to run-time binding of the implementation.

    6. Use bridge pattern to map orthogonal class hierarchies

    7. Bridge is designed up-front to let the abstraction and the implementation vary independently.

    
[Resources]:
    https://www.geeksforgeeks.org/bridge-design-pattern/

"""

from abc import ABC

class Renderer(ABC):
    def render_circle(self, radius):
        pass
    # render_square

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()