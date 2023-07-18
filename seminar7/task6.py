import random
import os

def generator_file_exs_folder(
    folder_dir, extensions, min_len=6, max_len=30, min_size=256, max_size=4096
):
    if not os.path.isdir(folder_dir):
        os.mkdir(folder_dir)
    os.chdir(folder_dir)
    for extension in extensions:
        for _ in range(extensions[extension]):
            check = True
            while check:
                name = ""
                for _ in range(random.randint(min_len, max_len)):
                    tmp = chr(random.randint(97, 122))
                    name = name + tmp
                if not os.path.isfile(f"{name}.{extension}"):
                    check = False
            with open(f"{name}.{extension}", "w", encoding="UTF-8") as f:
                for _ in range(random.randint(min_size, max_size)):
                    print(chr(random.randint(97, 122)), file=f, end='')

generator_file_exs_folder('tmp1', {'txt' : 1, 'pdf': 2})