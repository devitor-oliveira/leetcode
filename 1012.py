'''
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B. 
'''

pi = 3.14159
A, B, C = map(float, input().split(" "))

recTriangleArea:float = A * C / 2
circleArea:float = pi * C**2
trapeziumArea: float = (A + B) * C / 2
squareArea: float = B**2
recArea: float = A * B

print(f"TRIANGULO: {recTriangleArea:.3f}")
print(f"CIRCULO: {circleArea:.3f}")
print(f"TRAPEZIO: {trapeziumArea:.3f}")
print(f"QUADRADO: {squareArea:.3f}")
print(f"RETANGULO: {recArea:.3f}")