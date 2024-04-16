from .shape import Shape


class RightTriangle(Shape):
    def __init__(self, name,  odvesna1, odvesna2):
        super().__init__(name)
        self.odvesna1 = odvesna1
        self.odvesna2 = odvesna2

    def __str__(self):
        return f"Tento pravoúhlý trojůhelník se jmenuje {self.name} a má odvěsny {self.odvesna1}cm a {self.odvesna2}cm."

    def __float__(self):
        return (self.odvesna1 * self.odvesna2) / 2

    def __int__(self):
        return int(float(self))

    def calculate_area(self):
        return f"Obsah tohoto pravoúhlého trojúhelníku je {(self.odvesna1*self.odvesna2)/2}cm^2"
