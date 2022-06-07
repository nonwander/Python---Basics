#!/usr/bin/env python3
""">>>\nThe module raises a number to a negative power.
\tresult = x^y, where:
\tx > 0; x ∈ R
\ty < 0; y ∈ Z
\nThe User needs to enter value for real positive
number 'x' and a negative integer 'y'.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    def _validator(*args, **kwargs) -> Any

    get_input_values() -> tuple[float, int]

    my_func_power(x: float, y: int) -> float

    my_func_loop(x: float, y: int) -> float

    my_func_recursion(x: float, y: int) -> float

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
def get_input_values() -> tuple[float, int]:
    """Asks the user for the values of the arguments 'x', 'y'
    and returns them as a tuple of validated variables.

    Returns:
        Tuple[x, y], where:
            x -- a number raised to a power: x > 0; x ∈ R
            y -- a number that is a power value: y < 0; y ∈ Z
    """
    print('Enter a number raised to a power')
    x: float = float(input('x = '))
    print('Enter a value of power')
    y: int = int(input('y = '))
    if x > 0 and y < 0:
        return x, y
    else:
        raise ValueError(
            'Entered argument values must meet the following conditions:'
            + '\n\tx > 0; x ∈ R'
            + '\n\ty < 0; y ∈ Z,'
        )


def my_func_power(x: float, y: int) -> float:
    """Performs exponentiation using the ** operator.

    Arguments:
        x -- a number raised to a power: x > 0; x ∈ R
        y -- a number that is a power value: y < 0; y ∈ Z

    Returns:
        result -- the value of the result of raising 
                  the number 'x' to the power of 'y'.
    """
    result = x ** y
    return result


def my_func_loop(x: float, y: int) -> float:
    """Performs exponentiation using a loop.

    Arguments:
        x -- a number raised to a power: x > 0; x ∈ R
        y -- a number that is a power value: y < 0; y ∈ Z

    Returns:
        result -- the value of the result of raising 
                  the number 'x' to the power of 'y'.
    """
    value = x
    for _ in range(y, -1):
        value *= x
    result = 1 / value
    return result


def my_func_recursion(x: float, y: int) -> float:
    """Performs exponentiation using a recursion.

    Arguments:
        x -- a number raised to a power: x > 0; x ∈ R
        y -- a number that is a power value: y < 0; y ∈ Z

    Returns:
        the value of the result of raising the number 'x' to the power of 'y'.
    """
    if y == - 1:
        return (1/x)
    else:
        return (1/x * my_func_recursion(x, y + 1))


def main() -> None:
    """The execution point for the program file."""
    x, y = get_input_values()
    print(f'** operator is used: {my_func_power(x, y):.10f}')
    print(f'A loop is used:      {my_func_loop(x, y):.10f}')
    print(f'Recursion is used:   {my_func_recursion(x, y):.10f}')


if __name__ == '__main__':
    print(__doc__)
    main()
