#!/usr/bin/env python3
""">>>\nThis module determines the number of days after which an athlete will
achieve a given result in kilometers if he increases his result by 10% daily.

The User needs to enter the values of parameters a and b:
    a(int): kilometers, the result of the athlete on the first training day;
    b(int): kilometers, the desired result of the athlete.
Ounput to the screen:
    (int): the number of the day on which the athlete will achieve
           the specified result in kilometers

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_numbers() -> list[int]

    get_desired_day(input_numbers: list) -> int

    show_day(input_value: int) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""


from typing import Any, Callable


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
def get_input_numbers() -> list[int]:
    print('Enter the values of parameters a and b:'
        '\na(int): km, the result of the athlete on the first training day',
        '\nb(int): km, the desired result of the athlete'
    )
    input_a: str = input('a = ')
    a = int(input_a)
    input_b: str = input('b = ')
    b = int(input_b)
    if a <= 0 or b <= 0:
        raise ValueError(
            'entered number is out of range, must be a positive integer!'
        )
    return [a, b]


def get_desired_day(input_numbers: list) -> int:
    a, b = input_numbers
    result = a
    day = 1
    while True:
        if result >= b:
            break
        result += result * 0.1
        day += 1
    return day


def show_day(input_value: int) -> None:
    print(input_value)


def main() -> None:
    input_numbers: list[int] = get_input_numbers()
    desired_day: int = get_desired_day(input_numbers)
    show_day(desired_day)


if __name__ == '__main__':
    print(__doc__)
    main()
