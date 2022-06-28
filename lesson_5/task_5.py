#!/usr/bin/env python3
""">>>\nThis module working with text form file.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_validated_input_filename(input_filename: str) -> str

    create_file_get_sum(filename: str) -> int

Exceptions:
    FileExistsError, ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from random import randint

from typing import Any, Callable

from task_1 import get_validated_input_filename

DEFAULT_FILENAME = 'task_5.txt'


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
            except FileExistsError:
                print('',
                    '\nFile is already exists, can\'t open to write.',
                    '\nTry again!\n'
                )
            else:
                return result
    return _validator


def create_file_get_sum(filename: str) -> int:
    """_summary_

    Arguments:
        filename -- _description_

    Returns:
        _description_
    """
    max_value = 50
    max_len = 10
    with open(filename, 'w+') as f_obj:
        input_numbers = ' '.join(
            [str(randint(1, max_value)) for _ in range(max_len + 1)]
        )
        f_obj.write(input_numbers)
        f_obj.seek(0)
        content = f_obj.readline().split()
        sum_numbers = sum(map(int, content))
        print('File content: ', content)
        return sum_numbers


@validate_input
def main() -> None:
    """The execution point for the program file."""
    print('Enter the name for your data file:')
    print(f'Press "Enter" to write a file by default "{DEFAULT_FILENAME}"')
    input_filename = input()
    if input_filename:
        filename = get_validated_input_filename(input_filename)
    else:
        filename = DEFAULT_FILENAME
    print(create_file_get_sum(filename))


if __name__ == '__main__':
    print(__doc__)
    main()
