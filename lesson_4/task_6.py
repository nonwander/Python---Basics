#!/usr/bin/env python3
""">>>\nThis module ...

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    fact(n) -> list[int]

    show_iter_list(start, end) -> None

    show_cycle_list(input_list, end) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from itertools import count, cycle

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
    for idx in (range(n)):
        yield idx


def show_iter_list(start, end) -> None:
    for idx in count(start):
        if idx > end:
            break
        print(idx)


def show_cycle_list(input_list, end) -> None:
    for el in cycle(input_list):
        if end == 0:
            break
        print(el)
        end -= 1
    

def test_get_spec_list(func):
    test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    test_out = [12, 44, 4, 10, 78, 123]
    err_message = 'Function works uncorrect!'
    assert func(test_list) == test_out, f'{err_message}'


def main() -> None:
    """The execution point for the program file."""
    input_list = ['list']
    start = 3
    end = 10
    show_iter_list(start, end)
    show_cycle_list(input_list, end)

    
if __name__ == '__main__':
    print(__doc__)
    main()
