class ArgumentError(Exception):
    def __init__(self, value=None):
        self.value = value

    def __str__(self) -> str:
        return f"Не заданы параметры прямоугольника:\n{self.value if self.value is not None else ''}"


class NegativeValueError(Exception):
    def __init__(self, value=None):
        self.value = value

    def __str__(self) -> str:
        return f"Значение не может быть отрицательным:\n{self.value if self.value is not None else ''}"


class ZeroError(Exception):
    def __init__(self, value=None):
        self.value = value

    def __str__(self) -> str:
        return f"Значение параметра не может быть = 0\n{self.value if self.value is not None else ''}"
