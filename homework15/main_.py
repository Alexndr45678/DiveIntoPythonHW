from exceptions import ArgumentError, NegativeValueError, ZeroError


class Rectangle:
    def __init__(self, height=None, width=None):
        self.is_valid(height, width)
        if width is None or height is None:
            width = height if width is None else width
            height = width if height is None else height
        self.__height = height
        self.__width = width

    def get_area(self):
        return self.__width * self.__height

    def get_perimetr(self):
        return (self.__width + self.__height) * 2

    def __str__(self) -> str:
        return f"Прямоугольник {self.__width}X{self.__height}"

    @staticmethod
    def is_valid(height, width):
        if height is None and width is None:
            raise ArgumentError(f"{height=}{width=}")
        if (height is not None and height < 0) or (width is not None and width < 0):
            raise NegativeValueError(f"{f'{height=}'if height < 0 else f'{width=}'}")
        if (height is not None and height == 0) or (width is not None and width == 0):
            raise ZeroError(f"{f'{height=}' if height == 0 else f'{width=}'}")


if __name__ == "__main__":
    args = [
        {"height": None, "width": None},
        {"height": -1, "width": 3},
        {"height": 1, "width": -3},
        {"height": 1, "width": 0},
        {"height": 0, "width": 3},
        {"height": 3, "width": 5},
        {"height": 5, "width": None},
        {"height": None, "width": 6},
    ]
    lst = []
    for arg in args:
        try:
            lst.append(Rectangle(**arg))
        except (ArgumentError, ZeroError, NegativeValueError) as e:
            print(e)
        print()
    for i in lst:
        print(f"Периметр прямоугольника {i} = {i.get_perimetr()}")
        print(f"Площадь прямоугольника {i} = {i.get_area()}")
