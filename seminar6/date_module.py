import datetime
from calendar import isleap
import sys

__all__ = ["check_year", "check_date"]


def check_year(current_date):
    try:
        day, month, year = map(int, current_date.split("."))
    except:
        return False
    return isleap(year=year)


def check_date(current_date):
    try:
        day, month, year = map(int, current_date.split("."))
    except:
        return False

    try:
        datetime.datetime(year=year, month=month, day=day)
    except:
        return False
    return True


if __name__ == "__main__":
    print(check_date("14.11.1980"))
    print(check_year("12.05.2000"))

# def start_from_terminal():                # Раскомментировать для запуска из терминала.
#     date = sys.argv[1]                    # Команда для запуска: python .\seminar6\date_module.py DD.MM.YYYY
#     print(check_date(current_date=date))
#     print(check_year(current_date=date))
# start_from_terminal()
