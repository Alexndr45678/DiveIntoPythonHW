import random

def fill_file(name, count_lines):
    with open(name, 'a', encoding='utf-8') as f:
        for _ in range(count_lines):
            print(f'{random.randint(-1000, 1000)}|{random.uniform(-1000, 1000)}',file=f)

num = int(input("Введите количество строк:\n"))
fill_file('text.txt', num)