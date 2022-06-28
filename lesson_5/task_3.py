#!/usr/bin/env python3
""">>>\nThis module working with text form file.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_validated_input_filename(input_filename: str) -> str

    get_employee_statistics(filename: str) -> tuple[list[str], float]

Exceptions:
    FileExistsError, ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from typing import Any, Callable

from task_1 import get_validated_input_filename

DEFAULT_FILENAME = 'task_3.txt'


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


def get_employee_statistics(filename: str) -> tuple[list[str], float]:
    """Calculate some statistics about employee in file. 

    Arguments:
        filename -- name of file in curent directory.

    Returns:
        data of employee in tuple.
    """
    sum_salary: float = 0
    count: int = 0
    data_workers = list()
    with open(filename, 'r') as f_obj:
        for line in f_obj:
            employee, salary = line.split()
            if float(salary) < 20_000:
                data_workers.append(employee)
            sum_salary += float(salary)
            count += 1
    avg_salary = sum_salary / count
    return data_workers, avg_salary


@validate_input
def main() -> None:
    """The execution point for the program file."""
    print('Enter the name for your data file:')
    print(f'Press "Enter" to read a file by default "{DEFAULT_FILENAME}"')
    input_filename = input()
    if input_filename:
        filename = get_validated_input_filename(input_filename)
    else:
        filename = DEFAULT_FILENAME
    employees, avg_salary = get_employee_statistics(filename)
    print(
        f'{filename} statistics:',
        f'\n\tEmployees: {employees}',
        f'\n\tAverage salary: {avg_salary}',
    )


if __name__ == '__main__':
    print(__doc__)
    main()
