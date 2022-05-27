#!/usr/bin/env python3
""">>>\nThis module calculates an interesting value, which is similar
to the Droste Effect for the entered number.

Example:
    Input: 'n' belongs to the set N
    Output: int('n') + int('nn') + ... + int('n'^[n-1]) + int('n'^[n])
    *to create a sequence from the n-numbers of terms,
    is used string multiplication of the number n represented
    in string format and that is concatenation, not numerical
    multiplication!

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_number() -> int

    get_converted_number(input_number: int) -> int

    show_effect(input_value: int) -> None

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
    input_number = int(input_value)
    if input_number <= 0:
        raise ValueError(
            'entered number is out of range, must be a positive integer!'
        )
    return input_number


def get_converted_number(input_number: int) -> int:

    def recurcio(current_number: int) -> int:
        if len(str(current_number)) == 1:
            return current_number
        next_number = current_number // 10
        return recurcio(next_number) + current_number

    last_number = int(str(input_number) * input_number)
    return recurcio(last_number)


def show_effect(input_value: int) -> None:
    print(input_value)


def main() -> None:
    input_number: str = get_input_number()
    converted_number: dict = get_converted_number(input_number)
    show_effect(converted_number)


if __name__ == '__main__':
    print(__doc__)
    main()
