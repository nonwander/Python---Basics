#!/usr/bin/env python3
""">>>\nThis module demonstrates a custom class of a exception raises
if when by the division in function processed a divisor is equals to 0.

Classes:
    CustomZeroDivisionError(Exception)

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from typing import Any, Callable


class CustomZeroDivisionError(Exception):
    """This is the custom class of exception.
    Uses in division operation if divisor is zero.
    """
    def __init__(self, txt: str):
        self.txt: str = txt


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
def get_valid_input(input_value: str) -> float:
    """Converts User input string value to float number.

    Arguments:
        input_value -- User input value.

    Returns:
        number = float(input_value)
    """
    number: float = float(input_value)
    return number


def get_input_data() -> tuple[float, float]:
    print('Enter divisible value:')
    divisible: float = get_valid_input(input())
    print('Enter divisor value:')
    divisor: float = get_valid_input(input())
    return divisible, divisor


def get_quotient(divisible: float, divisor: float) -> float:
    try:
        if divisor == 0:
            raise CustomZeroDivisionError('can`t divide by zero!')
        else:
            quotient: float = divisible / divisor
            return quotient
    except CustomZeroDivisionError as err:
        print(f'Error: {err}')
        if input('Try enter values again? (y/n):') == 'y':
            main()
        else:
            exit(0)


def main() -> None:
    """The execution point for the program file."""
    divisible, divisor = get_input_data()
    quotient: float = get_quotient(divisible, divisor)
    print(f'{divisible} / {divisor} = {quotient:.3}')


if __name__ == '__main__':
    print(__doc__)
    main()
