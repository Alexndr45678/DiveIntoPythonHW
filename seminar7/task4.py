import random


def generator_file_exs(
    extension, min_len=6, max_len=30, min_size=256, max_size=4096, count_files=42
):
    for _ in range(count_files):
        name = ""
        for _ in range(random.randint(min_len, max_len)):
            tmp = chr(random.randint(97, 122))
            name = name + tmp
        with open(f"{name}.{extension}", "w", encoding="UTF-8") as f:
            for _ in range(random.randint(min_size, max_size)):
                print(chr(random.randint(97, 122)), file=f, end='')

generator_file_exs('txt', count_files=1)