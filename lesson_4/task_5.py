#!/usr/bin/env python3
""">>>\nThis module get numbers that are multiples of ```20``` or ```21```.
\nThe User needs to enter several parameters describing the User's data.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    generate_list(max_value: int, max_len: int) -> list[int]

    get_spec_list(start: int, end: int) -> list[int]

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from functools import reduce
from random import randint
from typing import Any, Callable


def validate_input(function) -> Callable[[], Any]:
    """Decorator for validating an incoming function.

    Arguments:
        function -- any incoming function.

    Returns:
        function -- validated function that returns an error-free result.
    """
    def _validator(*args, **kwargs) -> Any:
        """Wrapper function that monitors the ValueError.
        If the function being decorated fails, the wrapper
        function calls it again until it succeeds.

        Returns:
            result -- the result value of executing the decorated function.

        Exceptions:
            ValueError
        """
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
def generate_list(max_value: int, max_len: int) -> list[int]:
    """Requests the input value of an argument according to its name.

    Arguments:
        input_arg -- incoming argument.

    Returns:
        value -- string value of argument entered by User.
    """
    for _ in (range(max_len)):
        yield randint(1, max_value)


def get_spec_list(start: int, end: int) -> list[int]:
    """Accepts several named arguments as User's data
    and output them in one line.

    Arguments:

    Returns:
        args_in_line -- string line from User's data.
    """
    input_list = range(start, end + 1)
    spec_list: list[int] = reduce(
        lambda x, y: x * y,
        [el for el in range(start, end + 1)]
    )
    return spec_list


def test_get_spec_list():
    test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    test_out = [12, 44, 4, 10, 78, 123]
    err_message = 'Function works uncorrect!'
    assert get_spec_list(test_list) == test_out, f'{err_message}'


def main() -> None:
    """The execution point for the program file."""
    start = 100
    end = 1000
    output_list: list[int] = get_spec_list(start, end)
    print(output_list)


if __name__ == '__main__':
    print(__doc__)
    main()
