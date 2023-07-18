import random


def generator_file_exs(
    extensions, min_len=6, max_len=30, min_size=256, max_size=4096
):
    for extension in extensions:
        for _ in range(extensions[extension]):
            name = ""
            for _ in range(random.randint(min_len, max_len)):
                tmp = chr(random.randint(97, 122))
                name = name + tmp
            with open(f"{name}.{extension}", "w", encoding="UTF-8") as f:
                for _ in range(random.randint(min_size, max_size)):
                    print(chr(random.randint(97, 122)), file=f, end='')

generator_file_exs({'txt' : 1, 'pdf': 2})