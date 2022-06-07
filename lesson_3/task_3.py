#!/usr/bin/env python3
""">>>\nThis module takes three positional arguments and returns the sum
of the largest two arguments.
\nThe User needs to enter values of arguments separated by space.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_list() -> list[int]

    my_func(arg_1: int, arg_2: int, arg_3: int) -> int

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


@validate_input
def get_input_list() -> list[int]:
    """Asks the User for the values of three integer arguments
    and returns them as a tuple of validated variables.

    Raises:
        ValueError: an error is returned if the number of arguments
                    is not equal to three.

    Returns:
        output_list -- list of three integer type argument values.
    """
    input_line: str = input('Enter three arguments separated by space: ')
    output_list: list[int] = list(map(int, input_line.split()))
    if len(output_list) != 3:
        raise ValueError('number of arguments must be three!')
    return output_list


def my_func(
        arg_1: int, arg_2: int, arg_3: int
    ) -> int:
    """Takes three integer type positional arguments and returns the sum
    of the largest two arguments.

    Arguments:
        arg_1 -- first positional argument
        arg_2 -- second positional argument
        arg_3 -- third positional argument

    Returns:
        result -- sum of the largest two arguments.
    """
    arguments: dict[str, int] = locals()
    result: int = sum(arguments.values()) - min((arguments.values()))
    return result


def main() -> None:
    """The execution point for the program file."""
    arg_1, arg_2, arg_3 = get_input_list()
    print(my_func(
        arg_1, arg_2, arg_3
    ))


if __name__ == '__main__':
    print(__doc__)
    main()
