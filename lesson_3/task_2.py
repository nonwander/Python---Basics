#!/usr/bin/env python3
""">>>\nThis module generate string line from User's data.
\nThe User needs to enter several parameters describing the User's data.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_value(input_arg: str) -> Union[int, str]

    get_user_data(
        first_name: str,
        last_name: str,
        birth_year: int,
        residence_city: str,
        email: str,
        phonenumber: int
    ) -> str

Exceptions:
    ValueError

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
def get_input_value(input_arg: str) -> Union[int, str]:
    """Requests the input value of an argument according to its name.

    Arguments:
        input_arg -- incoming argument.

    Returns:
        value -- string value of argument entered by User.
    """
    value: str = input(f'{input_arg} = ')
    if input_arg in ('Birth year', 'Phonenumber'):
        return int(value)
    return value


def get_user_data(
        first_name: str,
        last_name: str,
        birth_year: int,
        residence_city: str,
        email: str,
        phonenumber: int
    ) -> str:
    """Accepts several named arguments as User's data
    and output them in one line.

    Arguments:
        first_name
        last_name
        birth_year
        residence_city
        email
        phonenumber

    Returns:
        args_in_line -- string line from User's data.
    """
    print('Enter User\'s data:')
    arguments: dict[str, str] = locals()
    args_in_line: str = ', '.join(
        f'{key}: {value}' for key, value in arguments.items()
    )
    return args_in_line


def main() -> None:
    """The execution point for the program file."""
    first_name: str = get_input_value('First name')
    last_name: str = get_input_value('Last name')
    birth_year: int = get_input_value('Birth year')
    residence_city: str = get_input_value('Residence city')
    email: str = get_input_value('email')
    phonenumber: int = get_input_value('Phonenumber')
    print(get_user_data(
        first_name,
        last_name,
        birth_year,
        residence_city,
        email,
        phonenumber
    ))


if __name__ == '__main__':
    print(__doc__)
    main()
