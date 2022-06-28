#!/usr/bin/env python3
""">>>\nThis module demonstrates a custom class of a Date.

NOTE: Validation of the date is conditional and does not check it
with the real one according to the Gregorian calendar. Because it
requires separate methods and voluminous code, taking into account
special cases.

Classes:
    Date

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
# TODO: Fix tests using "assert"


class Date:
    """This is the custom class of date.
    """
    def __init__(self, date_string: str) -> None:
        """Creates the date as a string .

        Arguments:
            date_string -- date in the 'day-month-year' format.
        """
        try:
            numbers: list[int] = Date.extract_numbers(date_string)
            self.validate_numbers(numbers)
            self.day, self.month, self.year = numbers
        except ValueError as err:
            print(f'Error: {err}')

    @classmethod
    def extract_numbers(cls, date_string: str) -> list[int]:
        """Extracts and onverts to integer type values of day, month and
        year from date in string type.

        Arguments:
            date_string -- string with date in the 'day-month-year' format.

        Returns:
            numbers -- integer numbers of date in list.
        """
        try:
            numbers: list[int] = [int(num) for num in date_string.split('-')]
        except ValueError:
            'entered numbers of date must be a positive integer!'
            numbers = [0, 0, 0]
        return numbers

    @staticmethod
    def validate_numbers(numbers: list) -> bool:
        """Validates numbers of day, month and year.

        Arguments:
            numbers -- integer numbers of date in list.

        Raises:
            ValueError: raises if the value of day is out of range;
            ValueError: raises if the value of month is out of range;
            ValueError: raises if the value of year is out of range.
        """
        dd, mm, yyyy = numbers
        try:
            if dd not in range(1, 31 + 1):
                raise ValueError(
                    'entered value of DAY is out of range!'
                )
            elif mm not in range(1, 12 + 1):
                raise ValueError(
                    'entered value of MONTH is out of range!'
                )
            elif yyyy not in range(1900, 3000):
                raise ValueError(
                    'entered value of YEAR is out of range!'
                )
            else:
                return True
        except ValueError as err:
            print(f'Error: {err}')
            return False


def test_module() -> None:
    """Testing the Module with output to the console."""
    data = {
        'incorrect_date': 'dd-mm-yyyy',
        'incorrect_date_day': '32-12-1990',
        'incorrect_date_month': '12-13-1990',
        'incorrect_date_year': '19-12-3990',
        'incorrect_date_format': '19:12:1990',
        'normal_date': '19-12-1990'
    }
    for name, date in data.items():
        print(f'\nInput:\n\t{name}: {date}')
        numbers = Date.extract_numbers(date)
        print(f'Out numbers:\n\t{numbers}')
        print(f'Validate {numbers}: {Date.validate_numbers(numbers)}')


def main() -> None:
    """The execution point for the program file."""
    test_module()


if __name__ == '__main__':
    print(__doc__)
    main()
