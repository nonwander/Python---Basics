#!/usr/bin/env python3
""">>>\nThis module demonstrate working with JSON type.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_firms_list(filename: str) -> tuple[dict[str, int], dict[str, int]]

    create_json(data, filename) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
import json

from typing import Any, Callable

from task_1 import get_validated_input_filename

DEFAULT_INPUT_FILENAME = 'task_7.txt'

DEFAULT_JSON_FILENAME = 'task_7.json'


def validate_func(function) -> Callable[[], Any]:
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


def get_firms_list(filename: str) -> tuple[dict[str, int], dict[str, int]]:
    """Creates a Python-object with dicts of firms' data.

    Arguments:
        filename -- validated input text file name

    Returns:
        Tuple[firms_list, avg_profit] -- tuple of firms' data
    """
    avg_profit: int = 0
    firms_list: dict[str, int] = dict()
    with open(filename, 'r') as f_obj:
        for data in f_obj:
            data = data.split()
            firm, form, revenue, costs = data
            profit = int(revenue) - int(costs)
            if profit > 0:
                avg_profit += profit
            firms_list.update({firm: profit})
        return firms_list, {'average_profit': avg_profit}


def create_json(data, filename) -> None:
    """Creates JSON file with summary firms' data.

    Arguments:
        data -- Python-object
        filename -- validated json file name
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


@validate_func
def main() -> None:
    """The execution point for the program file."""
    print('Enter the name for your data file:')
    print(
        'Press "Enter" to write a file by default',
        f'"{DEFAULT_INPUT_FILENAME}"'
    )
    input_filename = input()
    if input_filename:
        filename = get_validated_input_filename(input_filename)
    else:
        filename = DEFAULT_INPUT_FILENAME
    data = list(get_firms_list(filename))
    create_json(data, DEFAULT_JSON_FILENAME)
    print('>>>All done!')


if __name__ == '__main__':
    print(__doc__)
    main()
