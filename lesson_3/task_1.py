#!/usr/bin/env python3
""">>>\nThis module performs division of two arguments.
\nThe User needs to enter the values of the two arguments.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_numbers() -> tuple[float, float]

    get_division(argument_1: float, argument_2: float) -> Union[float, str]

Exceptions:
    ValueError, ZeroDivisionError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from typing import Any, Callable, Union


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
def get_input_numbers() -> tuple[float, float]:
    """Requests the User for two numbers,
    and returns them as a tuple of validated variables.

    Returns:
        output_list -- list of two float type argument values.
    """
    argument_1 = float(input('Enter value for argument_1: '))
    argument_2 = float(input('Enter value for argument_2: '))
    return argument_1, argument_2


def get_division(argument_1: float, argument_2: float) -> Union[float, str]:
    """Accepts two positional arguments and returns their division.

    Arguments:
        argument_1 -- first float type argument
        argument_2 -- second float type argument

    Returns:
        result -- result value of dividing arguments.

    Exceptions:
        ZeroDivisionError
    """
    try:
        result = argument_1/argument_2
    except ZeroDivisionError as err:
        return f'Error: {err}!'
    return result


def main() -> None:
    """The execution point for the program file."""
    argument_1, argument_2 = get_input_numbers()
    result_devision: Union[float, str] = get_division(argument_1, argument_2)
    print(result_devision)


if __name__ == '__main__':
    print(__doc__)
    main()
