# Создайте класс Матрица.
# Добавьте методы:
# вывода на печать,
# cравнения,
# сложения,
# *умножения матриц.
import random


class Matrix:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.matrix = [
            [random.randint(0, 9) for _ in range(rows)] for _ in range(columns)
        ]

    def __str__(self):
        return "\n".join([" ".join([str(i) for i in row]) for row in self.matrix])

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        result_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix)):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result_matrix.append(row)
        return Matrix(len(result_matrix), len(result_matrix))

    def __mul__(self, other):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other.matrix[0])):
                s = 0
                for k in range(len(other.matrix)):
                    s += self.matrix[i][k] * other.matrix[k][j]
                row.append(s)
            result.append(row)
        return Matrix(len(result), len(result))


m1 = Matrix(4, 4)
print(f"Первая матрица:\n{m1}\n")
m2 = Matrix(4, 4)
print(f"Вторая матрица:\n{m2}\n")
print(f"Сравнение матриц:\n{m1 == m2}\n")
print(f"Сложение матриц:\n{m1 + m2}\n")
print(f"Умножение матриц:\n{m1 * m2}\n")
