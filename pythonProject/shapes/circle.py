from .shape import Shape
import math


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def __str__(self):
        return f"Tento kruh se jmenuje {self.name} a má poloměr {self.radius}cm."

    def __float__(self):
        return math.pi * self.radius ** 2

    def __int__(self):
        return int(float(self))

    def calculate_area(self):
        return f"Obsah tohoto kruhu je {math.pi * self.radius ** 2}"

