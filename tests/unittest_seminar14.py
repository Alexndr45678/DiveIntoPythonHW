import unittest


class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b


class TestCheck(unittest.TestCase):
    def test_length1(self):
        c1 = Rectangle(4, 4)
        self.assertEqual(16, Rectangle.get_length(c1))

    def test_length2(self):
        c2 = Rectangle(5, 0)
        self.assertEqual(20, Rectangle.get_length(c2))

    def test_length1(self):
        c3 = Rectangle(10, 4)
        self.assertEqual(28, Rectangle.get_length(c3))


if __name__ == "__main__":
    unittest.main(verbosity=2)
