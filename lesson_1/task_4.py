#!/usr/bin/env python3
""">>>\nThis module finds the largest digit in the number entered by the user.
\nThe WHILE loop and arithmetic operations are used for the solution.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_number() -> int

    get_maximal_digit(input_number: int) -> int

    show_digit(input_value: int) -> None

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
def get_input_number() -> int:
    input_value: str = input('Enter number using a natural integer: ')
    number: int = int(input_value)
    if number <= 0:
        raise ValueError(
            'entered number is out of range, must be a positive integer!'
        )
    return number


def get_maximal_digit(input_number: int) -> int:
    maximal_digit = 0
    while input_number > 0:
        digit = input_number % 10
        input_number //= 10
        if digit > maximal_digit:
            maximal_digit = digit
    return maximal_digit


def show_digit(input_value: int) -> None:
    print(input_value)


def main() -> None:
    input_number: int = get_input_number()
    maximal_digit: int = get_maximal_digit(input_number)
    show_digit(maximal_digit)


if __name__ == '__main__':
    print(__doc__)
    main()
