# 1. Напишите программу, которая получает целое число и
# возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


# def convert_to_hex(n):
#     result = ""
#     s = "0123456789ABCDEF"
#     if n == 0:
#         return 0
#     while n > 0:
#         result = s[n % 16] + result
#         n = n // 16
#     return result


# num = int(input())
# print(f"{num} = {convert_to_hex(num)}")
# print("Проверка:", hex(num))


# 2. Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


def operation_with_fraction(fraction1, fraction2):
    num1, denom1 = int(fraction1[0]), int(fraction1[1])
    num2, denom2 = int(fraction2[0]), int(fraction2[1])

    sum_frac = f"{num1 * denom2 + num2 * denom1}/{denom1 * denom2}"
    prod_frac = f"{num1 * num2}/{denom1 * denom2}"

    return f"Сумма дробей: {sum_frac}\nПроизведение дробей: {prod_frac}"


frac1, frac2 = input().split(" "), input().split(" ")
print(operation_with_fraction(frac1, frac2))
