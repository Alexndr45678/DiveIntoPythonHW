import random


def func(name1, name2, name3):
    with open(name1, encoding="UTF-8") as f1, open(name2, encoding="UTF-8") as f2, open(
        name3, "w", encoding="UTF-8"
    ) as f3:
        text1 = f1.readlines()
        text2 = f2.readlines()
        len_max = max(len(text1), len(text2))
        i1 = 0
        i2 = 0
        for i in range(len_max):
            a, b = text1[i1].split("|")
            a = int(a)
            b = float(b)
            c = a * b
            name_tmp = text2[i2]
            if c < 0:
                print(f"{name_tmp.lower().strip()} {abs(c)}", file=f3)
            else:
                print(f"{name_tmp.upper().strip()} {round(c, 2)}", file=f3)
            i1 += 1
            i2 += 1
            if i1 >= len(text1):
                i1 = 0
            if i2 >= len(text2):
                i2 = 0


func('text.txt', 'rand.txt', 'result.txt')