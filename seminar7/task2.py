import random


def fill_file(name, count_lines):
    with open(name, "a", encoding="utf-8") as f:
        for j in range(count_lines):
            length = random.randint(4, 7)
            check = True
            while check:
                pswd = ""
                for i in range(length):
                    tmp = chr(random.randint(97, 122))
                    pswd = pswd + tmp
                    if tmp in ["a", "e", "o", "u", "i"]:
                        check = False
            print(pswd.capitalize(), file=f)


num = int(input("Введите количество строк:\n"))
fill_file("rand.txt", num)
