"""Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины."""


import math


class CircleException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f"Error: '{self.value}' должно быть > 0"


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_length(self):
        if self.radius < 0:
            raise CircleException(self.radius)
        return 2 * math.pi * self.radius

    def get_area(self):
        if self.radius < 0:
            raise CircleException(self.radius)
        return math.pi * self.radius**2


# first = Circle(int(input("Введите радиус круга:\n")))
# print(first.get_area())
# print(first.get_length())


class RectangleException(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = a if not b else b

    def __str__(self) -> str:
        return f"Стороны прямоугольника не могут быть отрицательными."


class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        if self.a < 0 or self.b < 0:
            raise RectangleException(self.a, self.b)
        return 2 * (self.a + self.b)

    def get_area(self):
        if self.a < 0 or self.b < 0:
            raise RectangleException(self.a, self.b)
        return self.a * self.b


# first = Rectangle(
#     int(input("Введите 1-ю сторону прямоугольника:\n")),
#     int(input("Введите 2-ю сторону прямоугольника:")),
# )
# print(first.get_length())
# print(first.get_area())
