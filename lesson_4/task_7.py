#!/usr/bin/env python3
""">>>\nThis module calculates factorial.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    fact(n) -> list[int]

    show_factorial(n) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
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


def fact(n) -> list[int]:
    """Requests the input value of an argument according to its name.

    Arguments:
        input_arg -- incoming argument.

    Returns:
        value -- string value of argument entered by User.
    """
    result = 1
    for idx in range(1, n + 1):
        result *= idx
        yield result


def show_factorial(n) -> None:
    for el in fact(n):
        print(el)


def test_get_spec_list(func):
    test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    test_out = [12, 44, 4, 10, 78, 123]
    err_message = 'Function works uncorrect!'
    assert func(test_list) == test_out, f'{err_message}'


def main() -> None:
    """The execution point for the program file."""
    show_factorial(10)


if __name__ == '__main__':
    print(__doc__)
    main()
