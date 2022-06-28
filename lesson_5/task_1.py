#!/usr/bin/env python3
""">>>\nThis modile creates a file with data entered by User line by line.
An empty input line means the end of the file and the recording is terminated.

File extensions are available to the User:
    %s

NOTE: The file type is not determined by the extension on UNIX systems.
The file extension is just a visual indicator for people.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_validated_input_filename(input_filename: str) -> str

    write_unique_file(filename: str) -> None

Exceptions:
    FileExistsError, ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from typing import Any, Callable

ALLOWED_EXTENTIONS: list[str] = [
    'txt',
    'py',
    'json',
    'sh',
]

FORBIDDEN_CHARS: list[str] = [
    '-', '/', '\\', '?', '<', '>', '*', '|', '"',
]

DEFAULT_FILENAME = 'task_1.txt'


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


def get_validated_input_filename(input_filename: str) -> str:
    """Validates the input value of the file name and returns it
    or returns the default name if it is empty.
    Input file name can be with or without an extention.
    All spaces are basically replaced with an underscore.

    Arguments:
        input_filename -- not validated input file name

    Raises:
        ValueError: raises, if entered extention is not allowed
        ValueError: raises, if '-' is used at the beginning of a file name
        ValueError: raises, if entered file name is not corrected

    Returns:
        validated_name: str -- '{filename}.{ext}'
    """
    input_filename = input_filename.replace(' ', '_')
    if input_filename.count('.') == 1:
        filename, ext = input_filename.split('.')
        if ext not in ALLOWED_EXTENTIONS:
            raise ValueError(f'*.{ext} not allowed extention for file!')
        elif filename[0] == FORBIDDEN_CHARS[0]:
            raise ValueError('symbol "-" cannot be used at the beginning of a file name!')  # noqa flake8
        for char in filename:
            if char in FORBIDDEN_CHARS[1:]:
                raise ValueError(f'symbol "{char}" is not allowed char in filename!')  # noqa flake8
        else:
            validated_name = input_filename
    elif input_filename.count('.') == 0:
        validated_name = '.'.join([input_filename, ALLOWED_EXTENTIONS[0]])
    else:
        raise ValueError('filename is not corrected!')
    return validated_name


def write_unique_file(filename: str) -> None:
    with open(filename, 'x') as f_obj:
        print(
            f'{filename} is ready to writing.',
            'Now you can enter your data.'
        )
        while True:
            user_line = input('->')
            if user_line == '':
                break
            print(user_line, file=f_obj)


@validate_input
def main() -> None:
    """The execution point for the program file."""
    print('Enter the name for your data file:')
    print(f'Press "Enter" to create a file by default "{DEFAULT_FILENAME}"')
    input_filename = input()
    if input_filename:
        filename = get_validated_input_filename(input_filename)
    else:
        filename = DEFAULT_FILENAME
    write_unique_file(filename)
    print(f'{filename} is written and closed.')


if __name__ == '__main__':
    __doc__ %= ', '.join(['*.' + el for el in ALLOWED_EXTENTIONS])
    print(__doc__)
    main()
