from shapes import *

c1 = Circle("Kruh1", 2)
r1 = Rectangle("Obdélník1", 2, 5)
t1 = Trapezoid("Lichobežník1", 3, 4, 2)
rt1 = RightTriangle("Pravoúhlý trojúhelník1", 3, 4)


print(c1.calculate_area())
print(r1.calculate_area())
print(t1.calculate_area())
print(rt1.calculate_area())

print()
print(c1)
print(r1)
print(t1)
print(rt1)

print()
print(int(r1) + int(t1))
print(int(c1))
print(float(c1))
print(float(c1) + int(r1))