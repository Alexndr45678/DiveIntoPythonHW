""" 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

# import os

# def get_file_info(path):
#     file_path, file_name = os.path.split(path)
#     file_name, file_extension = os.path.splitext(file_name)
#     return (file_path, file_name, file_extension)

# path_to_file = input('Введите путь к файлу:\n')
# print(get_file_info(path_to_file))



"""2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии."""


# names = ["Alice", "Bob", "Charlie"]
# rates = [1000, 2000, 3000]
# bonuses = ["10.25%", "5.5%", "7.75%"]

# result = {name: rate * float(bonus.strip("%")) / 100 for name, rate, bonus in zip(names, rates, bonuses)}
# print(result)




# 3. Создайте функцию генератор чисел Фибоначчи.

# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# fibonacci = fibonacci_generator()
# for i in range(int(input("Введите число:\n"))):
#     print(next(fibonacci))