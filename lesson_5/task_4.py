#!/usr/bin/env python3
""">>>\nThis module working with text form file.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_validated_input_filename(input_filename: str) -> str

    get_rus_dict(en_filename: str, ru_filename) -> None

Exceptions:
    FileExistsError, ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from typing import Any, Callable

from task_1 import get_validated_input_filename

DEFAULT_EN_FILENAME = 'task_4_in.txt'

DEFAULT_RUS_FILENAME = 'task_4_out.txt'

NUMERIC_DICT = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Zero': 'Ноль'
}


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


def get_rus_dict(en_filename: str, ru_filename) -> None:
    """Traslates input data according to simle dictionary in code
    and records new data in a new file.

    Arguments:
        filename -- name of file in curent directory.
    """
    with open(en_filename, 'r') as f_en, open(ru_filename, 'w') as f_ru:
        for line_en in f_en:
            line_en = line_en.rstrip('\n').split(' — ')
            if line_en[0] in NUMERIC_DICT.keys():
                line_ru = ' — '.join([NUMERIC_DICT[line_en[0]], line_en[1]])
                print(line_ru, file=f_ru)


@validate_input
def main() -> None:
    """The execution point for the program file."""
    print('Enter the name for your data file:')
    print(f'Press "Enter" to read a file by default "{DEFAULT_EN_FILENAME}"')
    input_filename = input()
    if input_filename:
        en_filename = get_validated_input_filename(input_filename)
    else:
        en_filename = DEFAULT_EN_FILENAME
    print(f'Press "Enter" to write a file by default "{DEFAULT_RUS_FILENAME}"')
    input_filename = input()
    if input_filename:
        ru_filename = get_validated_input_filename(input_filename)
    else:
        ru_filename = DEFAULT_RUS_FILENAME
    get_rus_dict(en_filename, ru_filename)


if __name__ == '__main__':
    print(__doc__)
    main()
