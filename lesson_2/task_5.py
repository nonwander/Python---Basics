#!/usr/bin/env python3
""">>>\nThis module returns the list of raiting values.
Raiting list is a decreasing list of natural numbers.
The User needs to enter the value of the raiting in range [1 .. 10].

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_value() -> int

    get_raiting_list(input_value: int) -> list[int]

    show_raiting_list(input_value: list[int]) -> None

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
def get_input_value() -> int:
    input_value: str = input('Enter raiting vlue using a natural integer: ')
    value = int(input_value)
    if value not in range(1, 10 + 1):
        raise ValueError(
            'entered number is out of range, must be a positive integer!'
        )
    return value


def get_raiting_list(input_value: int) -> list[int]:
    initial_list: list[int] = [7, 5, 3, 3, 2]
    initial_list.append(input_value)
    initial_list.sort(reverse=True)
    return initial_list


def show_raiting_list(input_value: list[int]) -> None:
    print(input_value)


def main() -> None:
    input_value: int = get_input_value()
    raiting_list: list[int] = get_raiting_list(input_value)
    show_raiting_list(raiting_list)


if __name__ == '__main__':
    print(__doc__)
    main()
