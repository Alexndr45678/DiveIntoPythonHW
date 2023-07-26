import csv
import json
import random


def generate_csv_file(filename: str, count_lines: int):
    with open(f"{filename}.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for _ in range(count_lines):
            lines = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(lines)


name = input("Введите название csv файла:\n")
num = random.randint(100, 1000)
generate_csv_file(name, num)


def run_on_csv(func):
    def wrapper(file_path):
        with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                return f"Для переменных {a}, {b}, {c} корни = {result}"

    return wrapper


def save_to_json(func):
    def wrapper(*args):
        result = func(*args)
        data = {"args": args, "result": result}
        with open(f"{func.__name__}.json", "w") as jsonfile:
            json.dump(data, jsonfile)
        return result

    return wrapper


@save_to_json
def find_roots(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return (-b / (2 * a),)
    else:
        return (
            (-b + discriminant**0.5) / (2 * a),
            (-b - discriminant**0.5) / (2 * a),
        )


find_roots(1, 2, 1)
