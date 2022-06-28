#!/usr/bin/env python3
""">>>\nThis module calculate a sum of all numbers in input string line.

Instructions:
The User needs to enter numbers in one line separated by a space.
After pressing Enter the program calculate the sum of entered numbers.
The sum can be calculated continiously while User not enter reserved
instruction '\q'.

Functions:

    main() -> None

    get_sum() -> float

    get_input_line() -> list[str]

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
def get_sum() -> float:
    """Calculates a sum of all numbers in input string line.

    Returns:
        sum -- sum of all numbers in input string line
    """
    def get_input_line() -> list[str]:
        """Requests User input and returns a string.

        Returns:
            input_line -- list of string-typed user's input numbers
        """
        print('Enter numbers separated by a space or \'\q\' to exit:')
        input_line: list[str] = input().split()
        return input_line

    sum: float = 0
    while True:
        input_line: list[str] = get_input_line()
        for elem in input_line:
            if elem == '\q':
                print(sum)
                return sum
            else:
                try:
                    sum += float(elem)
                except ValueError:
                    print(f'{elem} is a non-numeric value.')
        print(sum)


def main() -> None:
    """The execution point for the program file."""
    get_sum()


if __name__ == '__main__':
    print(__doc__)
    main()
