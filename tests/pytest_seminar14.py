import pytest


class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b


def first_test():
    c1 = Rectangle(4, 4)
    assert 16 == Rectangle.get_length(c1)


def second_test():
    c2 = Rectangle(5, 0)
    assert 48 == Rectangle.get_length(c2)


def third_test():
    c3 = Rectangle(10)
    assert 28 == Rectangle.get_length(c3)


if __name__ == "__main__":
    pytest.main(["-v"])
