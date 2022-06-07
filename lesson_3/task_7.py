#!/usr/bin/env python3
""">>>\nThis module is a continuation of module task_6,
so you need to use them together.

It converts all Latin words in input text to uppercase first letter.
\nThe User needs to enter text in line.

Functions:

    main() -> None

    get_input_text() -> str

Exceptions:
    ImportError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
try:
    from task_6 import int_func
except ImportError as err:
    print('Error: ',
        err,
        '\nThis module is a continuation of module task_6,',
        'check that they are in the same directory.'
    )
    exit(1)

def get_input_text() -> str:
    """Requests User input and returns a string.

    Returns:
        text: str -- user's input string
    """
    print('Enter one or several words separated by space:')
    text: str = input()
    return text


def main() -> None:
    """The execution point for the program file."""
    input_text = get_input_text()
    print(int_func(input_text))


if __name__ == '__main__':
    print(__doc__)
    main()
