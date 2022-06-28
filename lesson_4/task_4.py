#!/usr/bin/env python3
""">>>\nThis module generate string line from User's data.
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


def get_spec_list(max_value: int, max_len: int) -> list[int]:
    """Accepts several named arguments as User's data
    and output them in one line.

    Arguments:

    Returns:
        args_in_line -- string line from User's data.
    """
    test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    input_list = test_list
    spec_list: list[int] = [el for el in input_list if input_list.count(el) == 1]
    return spec_list


def test_get_spec_list():
    test_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    test_out = [23, 1, 3, 10, 4, 11]
    err_message = 'Function works uncorrect!'
    assert get_spec_list(test_list) == test_out, f'{err_message}'


def main() -> None:
    """The execution point for the program file."""
    output_list: list[int] = get_spec_list(300, 10)
    print(output_list)


if __name__ == '__main__':
    print(__doc__)
    main()
