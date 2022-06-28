#!/usr/bin/env python3
""">>>\nThis module demonstrate working with text form file.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_dict_study_plan(filename: str) -> dict

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from itertools import groupby

from typing import Any, Callable

from task_1 import get_validated_input_filename

DEFAULT_FILENAME = 'task_6.txt'


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


def get_dict_study_plan(filename: str) -> dict:
    """Getting summary study plan from txt-file.

    Arguments:
        filename -- validated input text file name

    Returns:
        study_plan -- dict with summary study plan
    """
    study_plan: dict = dict()
    with open(filename, 'r') as f_obj:
        for line in f_obj:
            sum_classes = 0
            line = line.split()
            subj, *classes = line
            for item in classes:
                if item is not '-' and item is not '—':
                    sum_classes += int(
                        [''.join(number) for _, number in groupby(
                            item, key = lambda x: x.isdigit()
                        )][0]
                    )
            study_plan.update({subj[:-1]: sum_classes})
        return study_plan


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
    print(get_dict_study_plan(filename))


if __name__ == '__main__':
    print(__doc__)
    main()
