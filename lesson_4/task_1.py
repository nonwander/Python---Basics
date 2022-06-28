#!/usr/bin/env python3
""">>>\nThis module calculates the employee's salary using the formula:
PRODUCTIVITY(hours) * RATE(per hour) + PREMIUM

The script must be run with the parameters of the values used.

[300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
--> [12, 44, 4, 10, 78, 123]

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_numbers() -> tuple[float, float]

    get_division(argument_1: float, argument_2: float) -> Union[float, str]

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from sys import argv


def get_input_args() -> tuple[float, float, float]:
    """Gets the arguments passed into the file in the command line,
    and returns them as a tuple of validated variables.

    Returns:
        list of three float type argument values:

    """
    productivity_h, rate_h, premium = map(float, argv[1:])
    return productivity_h, rate_h, premium


def get_salary(employee_args: tuple[float, float, float]) -> float:
    """Accepts three positional arguments and returns employee's salary.

    Arguments:
        employee_args[0] -- employee's productivity in hours
        employee_args[1] -- employee's rate per hour
        employee_args[2] -- employee's premium 

    Returns:
        result -- employee's salary.
    """
    result: float = employee_args[0] * employee_args[1] + employee_args[2]
    return result


def main() -> None:
    """The execution point for the program file."""
    employee_args: tuple[float, float, float] = get_input_args()
    salary: float = get_salary(employee_args)
    print(salary)


if __name__ == '__main__':
    print(__doc__)
    main()
