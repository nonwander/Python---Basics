#!/usr/bin/env python3
""">>>\nThis module demonstrates a custom class of a exception raises
when processed by the function a non-numeric type of element.

Classes:
    NumberValueException(Exception)

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
class NumberValueException(Exception):
    """This is the custom class of exception.
    Uses to inappropriate argument value (of correct type).
    """
    def __init__(self, txt: str):
        self.txt: str = txt


def get_list_numbers() -> list[float]:
    """Creates a list of validated numbers from the entered string.

    Returns:
        number_list -- list of numbers only in input string line.
    """
    def get_input_line() -> list[str]:
        """Requests User input and returns a list of string typed elements.

        Returns:
            input_line -- list of string-typed User's input elements.
        """
        print('Enter numbers separated by a space or \'\q\' to exit:')
        input_list: list[str] = input().split()
        return input_list

    def incert_number_to_list(elem: str) -> None:
        """Checks the current list item and adds it to the list if
        the item is a number.

        Arguments:
            elem -- a current string type list item.

        Raises:
            NumberValueException: custom exception that raises when processed
                by the function a non-numeric type of element.
        """
        nonlocal list_of_numbers
        try:
            list_of_numbers.append(float(elem))
        except ValueError:
            raise NumberValueException(
                f'{elem} is a non-numeric value!'
            )

    list_of_numbers: list[float] = []
    while True:
        input_line: list[str] = get_input_line()
        for elem in input_line:
            if elem == '\q':
                return list_of_numbers
            else:
                try:
                    incert_number_to_list(elem)
                except NumberValueException as err:
                    print(f'Error: {err}')
        print(list_of_numbers)


def main() -> None:
    """The execution point for the program file."""
    print('The final list of numbers:', get_list_numbers())


if __name__ == '__main__':
    print(__doc__)
    main()
