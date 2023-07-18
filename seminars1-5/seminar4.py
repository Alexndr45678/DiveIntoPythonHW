# 1. Напишите функцию для транспонирования матрицы.


# def matrix_tranposition(matr):
#     trans_m = [[0 for _ in range(len(matr))] for _ in range(len(matr))]
#     for i in range(len(matr)):
#         for j in range(len(matr)):
#             trans_m[i][j] = matr[j][i]
#     return trans_m


# default_matrix = [[j for j in range(1, 4)] for _ in range(1, 4)]
# trans = matrix_tranposition(default_matrix)
# print("Транспонированная матрица:", *trans, sep="\n")


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


# def my_func(**kwargs) -> dict:
#     dict_args = {}
#     for key, val in kwargs.items():
#         dict_args[str(val)] = key
#     return dict_args


# print(my_func(a='qwert', b=2, c=3))


# 3. Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

""" Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег"""

bank = 0
count = 0


def top_up_balance(cash):
    global bank, count
    bank += cash
    count += 1
    return print(f"Баланс: {bank}")


def withdrow_money(cash):
    global bank, count
    if cash < bank:
        if (bank / 100 * 1.5) < 30:
            bank - +30
        elif 30 < (bank / 100 * 1.5) < 600:
            bank -= bank / 100 * 1.5
        elif (bank / 100 * 1.5) > 600:
            bank -= 600
    else:
        return "Недостаточно средств."

    bank -= cash
    count += 1
    return print(f"Баланс: {bank}")


def exit_bank():
    print("Вы вышли из банка")
    exit()


def check_balance():
    while True:
        cash = int(input("Введите сумму кратную 50:\n"))
        if cash % 50 == 0:
            return cash


while True:
    move = input("Выберите действие:\n1 - Пополнить баланс\n2 - Снять деньги\n3 - Выход\n")
    if bank >= 5_000_000:
        bank *= 0.9
        
    match move:
        case '1':
            top_up_balance(check_balance())
        
        case '2':
            withdrow_money(check_balance())
            
        case '3':
            exit_bank()
            
    
    if count == 3:
        bank *= 1.03
        count = 0