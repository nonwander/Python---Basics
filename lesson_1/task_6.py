#!/usr/bin/env python3
""">>>\nThis module is a continuation of module task_5,
so you need to use them together.

It calculates company`s profitability of revenue and the level of labor
productivity in the company. Finally it displays the result on the screen.

The User needs to enter the value of the number of employees of the company.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_profitability(performance, input_indicators) -> float

    get_employees_number() -> int

    get_profit_per_employee(performance, employees) -> float

    show_result(profitability, profit_per_employee) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""


try:
    import task_5
except ImportError as err:
    print('Error: ',
        err,
        '\nThis module is a continuation of module task_5,',
        'check that they are in the same directory.'
    )
    exit(1)

from typing import Any, Callable


def validate_input(function) -> Callable[[], Any]:
    def _validator(*args, **kwargs) -> Any:
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


def get_profitability(performance, input_indicators) -> float:
    revenue, *args = input_indicators
    profitability: float = performance / revenue
    return profitability


@validate_input
def get_employees_number() -> int:
    input_value: str = input('Enter company`s number of employees: ')
    employees_number = int(input_value)
    if employees_number <= 0:
        raise ValueError(
            'entered number is out of range, must be a positive integer!'
        )
    return employees_number


def get_profit_per_employee(performance, employees) -> float:
    profit_per_employee: float = performance / employees
    return profit_per_employee


def show_result(profitability, profit_per_employee) -> None:
    text_profitability: str = 'The company`s profitability of revenue is:'
    text_profit_per_employee: str = (
        'The level of labor productivity in the company is:'
    )
    print(f'{text_profitability} {profitability}')
    print(f'{text_profit_per_employee} {profit_per_employee}')


def main() -> None:
    performance, indicators = task_5.main()
    if performance > 0:
        profitability: float = get_profitability(
            performance, indicators
        )
        employees: int = get_employees_number()
        profit_per_employee: float = get_profit_per_employee(
            performance, employees
        )
        show_result(profitability, profit_per_employee)


if __name__ == '__main__':
    print(__doc__)
    main()
