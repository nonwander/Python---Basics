#!/usr/bin/env python3
""">>>\nThis module calculates the financial result of the company
and displays the conclusion on the screen.

The User needs to enter the values of the company's performance indicators.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_data() -> list

    get_company_performance(input_indicators: list[float]) -> float

    show_result(company_performance: int) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""


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


@validate_input
def get_input_data() -> list:
    print('Enter the values of the company`s revenue and costs:')
    input_revenue: str = input('revenue = ')
    input_costs: str = input('costs = ')
    revenue = float(input_revenue)
    costs = float(input_costs)
    return [revenue, costs]


def get_company_performance(input_indicators: list[float]) -> float:
    revenue, costs = input_indicators
    perfomance = revenue - costs
    return perfomance


def show_result(company_performance: int) -> None:
    if company_performance > 0:
        result = 'Good perfomance:'
    elif company_performance == 0:
        result = 'Bad perfomance:'
    else:
        result = 'Very bad perfomance:'
    print(f'{result} {company_performance}')


def main() -> list:
    input_indicators: list[float] = get_input_data()
    company_performance: float = get_company_performance(input_indicators)
    show_result(company_performance)
    return [company_performance, input_indicators]


if __name__ == '__main__':
    print(__doc__)
    main()
