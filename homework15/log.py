import logging
import argparse
from pathlib import Path
from exceptions import ArgumentError, NegativeValueError, ZeroError
import main_


def get_logger(filename=f"homework15/{'data.log'}"):
    if not Path.cwd().is_dir():
        Path.cwd().mkdir()
    logging.basicConfig(
        filename=filename,
        filemode="a",
        encoding="UTF-8",
        level=logging.DEBUG,
        style="{",
        format="{asctime} {levelname} {funcName}: {msg}",
    )
    return logging.getLogger()


logger = get_logger()

if __name__ == "__main__":
    parse = argparse.ArgumentParser(
        description="Периметр и площадь по заданным параметрам"
    )
    parse.add_argument(
        "-W", type=float, metavar="width", nargs="?", default=None, help="Ширина"
    )
    parse.add_argument(
        "-H", type=float, metavar="height", nargs="?", default=None, help="Высота"
    )
    args = parse.parse_args()
    try:
        r1 = main_.Rectangle(height=args.H, width=args.W)
        logger.info(f"Создан: {str(r1).lower()}")
        print(f"Периметр: {r1.get_perimetr()}")
        print(f"Площадь: {r1.get_area()}")

    except (ArgumentError, ZeroError, NegativeValueError) as e:
        print(e)
        logger.warning(e)
