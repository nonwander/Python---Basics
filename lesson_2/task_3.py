#!/usr/bin/env python3
""">>>\nThis module returns the time of year according to entered month number
(winter, spring, summer, autumn).
\nThe User needs to enter the number of the month as an integer from 1 to 12.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_month_number() -> int

    get_time_of_year(month_number: int) -> str

    show_time_of_year(input_value: str) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from typing import Any, Callable

MONTH_DICT = {
    'winter': [1, 2, 12],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}


def validate_input(function) -> Callable[[], Any]:
    def _validator(*args, **kwargs) -> Any:
        while True:
            try:
                result = function(*args, **kwargs)
            except ValueError as err:
                print('',
                    '\nError: ', err,
                    '\nTry again!\n'
                )
            else:
                return result
    return _validator


@validate_input
def get_month_number() -> int:
    input_value: str = input('Enter month number using a natural integer: ')
    month_number = int(input_value)
    if month_number not in range(1, 12 + 1):
        raise ValueError(
            'entered number is out of range, must be a positive integer!'
        )
    return month_number


def get_time_of_year(month_number: int) -> str:
    for year_time, month in MONTH_DICT.items():
        if month_number in month:
            break
    return year_time


def show_time_of_year(input_value: str) -> None:
    print(input_value)


def main() -> None:
    month_number: int = get_month_number()
    time_of_year: str = get_time_of_year(month_number)
    show_time_of_year(time_of_year)


if __name__ == '__main__':
    print(__doc__)
    main()
