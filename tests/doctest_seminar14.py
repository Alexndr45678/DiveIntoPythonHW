import doctest


class Rectangle:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        """
        >>> c1 = Rectangle(4, 4)
        >>> Rectangle.get_length(c1)
        16
        >>> c2 = Rectangle(5,0)
        >>> Rectangle.get_length(c2)
        20
        >>> c3 = Rectangle(10,4)
        >>> Rectangle.get_length(c3)
        28
        """
        return 2 * (self.a + self.b)

    def get_area(self):
        """ 
        >>> c1 = Rectangle(4,4)
        >>> Rectangle.get_area(c1)
        16
        >>> c2 = Rectangle(5,1)
        >>> Rectangle.get_area(c2)
        5
        >>> c3 = Rectangle(10,4)
        >>> Rectangle.get_area(c3)
        40
        """
        return self.a * self.b

doctest.testmod(verbose=True)
