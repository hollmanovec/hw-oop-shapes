from .shape import Shape


class Rectangle(Shape):
    def __init__(self, name, a, b):
        super().__init__(name)
        self.a = a
        self.b = b

    def __str__(self):
        return f"Tento obdélník se jmenuje {self.name} a má strany {self.a}cm a {self.b}cm."

    def __int__(self):
        return self.a * self.b

    def calculate_area(self):
        return f"Obsah tohoto obdélníku je {self.a * self.b}cm^2."