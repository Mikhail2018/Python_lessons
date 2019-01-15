# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle():
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.AB = math.sqrt(((bx - ax) ** 2) + ((by - ay) ** 2))
        self.AC = math.sqrt(((cx - ax) ** 2) + ((cy - ay) ** 2))
        self.BC = math.sqrt(((cx - bx) ** 2) + ((cy - by) ** 2))

    def perimeter(self):
        self.perimeter = round(self.AB + self.AC + self.BC, 2)
        return (self.perimeter)

    def square(self):
        self.square = abs(((((self.bx - self.ax) * (self.cy - self.ay)) - ((self.cx - self.ax) * (self.by - self.ay))) / 2))
        return (self.square)

    def height(self):
        self.square *= 2
        self.height = round((self.square / self.AC), 2)
        return (self.height)


triangle = Triangle(-2,-6, -6, -3, 10, -1)
c = triangle.perimeter()
s = triangle.square()
v = triangle.height()
print('\nПериметр треугольника АВС: ', c)
print('Площадь треугольника АВС: ', s)
print('Высота треугольника АВС: ', v)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium():
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.dx = dx
        self.dy = dy
        self.t = Triangle(ax, ay, bx, by, cx, cy)
        self.AD = math.sqrt(((dx - ax) ** 2) + ((dy - ay) ** 2))
        self.CD = math.sqrt(((dx - cx) ** 2) + ((dy - cy) ** 2))
        self.BD = math.sqrt(((dx - bx) ** 2) + ((dy - by) ** 2))

    def check_trapezium(self):
        if round(z.t.AC, 2) == round(z.BD, 2):
            self.check_trapezium = True
        else:
            self.check_trapezium = False
        return (self.check_trapezium)

    def perimeter(self):
        self.perimeter = round((self.t.AB + self.t.BC + self.CD + self.AD), 2)
        return (self.perimeter)

    def square(self):
        self.square = ((z.t.BC + z.AD) / 4) * (math.sqrt((4* (z.t.AB ** 2)) - ((z.t.BC - z.AD)**2)))
        return (self.square)

z = Trapezium(0, 0, 3, 5, 11, 5, 14, 0)

a = round(z.t.AB, 2)
b = round(z.t.BC, 2)
c = round(z.CD, 2)
d = round(z.AD, 2)

print('\nЯвляется ли фигура равнобочной трапецией: {}'.format(z.check_trapezium()))
print('Длинны сторон А: {} B: {} C: {} D: {}'.format(a, b, c, d))
print('Периметр трапеции: {}'.format(z.perimeter()))
print('Площадь трапеции: {}'.format(z.square()))