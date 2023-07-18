"""1. Напишите функцию группового переименования файлов. Она должна:

1 - Принимать параметр желаемое конечное имя файлов.
    При переименовании в конце имени добавляется порядковый номер.
2 - Принимать параметр количество цифр в порядковом номере.
3 - Принимать параметр расширение исходного файла. 
    Переименование должно работать только для этих файлов внутри каталога.
4 - Принимать параметр расширение конечного файла.
5 - Принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
    К ним прибавляется желаемое конечное имя, если оно передано. 
    Далее счётчик файлов и расширение."""


import os


def rename_file(name, num_digits, ext, final_ext, from_name=0, to_name=0):
    count = 1
    files = [
        f
        for f in os.listdir(os.getcwd())
        if os.path.isfile(os.path.join(os.getcwd(), f))
    ]
    print(files)

    for file in files:
        if file.split(".")[-1] == ext:
            name_file = file.split(".")[0][from_name:to_name]
            if len(str(count)) != num_digits:
                tmp = (num_digits - len(str(count))) * "0"
                file_count = f"{tmp}{count}"
                print(file_count)
            result_name = f"{name_file}{name}{file_count}.{final_ext}"
            print(file)
            os.rename(file, result_name)
            print(result_name)
            count += 1


if __name__ == "__main__":
    rename_file("file", 5, "txt", "md", 0, 0)
