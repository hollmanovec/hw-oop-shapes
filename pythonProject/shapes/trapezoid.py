from .shape import Shape


class Trapezoid(Shape):
    def __init__(self, name, a, b, vyska):
        super().__init__(name)
        self.a = a
        self.b = b
        self.vyska = vyska

    def __str__(self):
        return f"Tento lichoběžník se jmenuje {self.name}, strany má {self.a}cm a {self.b}cm a výšku má {self.vyska}cm."

    def __float__(self):
        return ((self.a * self.b) / 2) * self.vyska

    def __int__(self):
        return int(float(self))

    def calculate_area(self):
        return f"Obsah tohoto lichoběžníku je {((self.a * self.b)/2) * self.vyska} cm^2."
