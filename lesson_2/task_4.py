#!/usr/bin/env python3
""">>>\nThis module prints each word of a entered line 
from a new line and numbers them.
The User needs to enter words in input line separated by a space.

Functions:

    main() -> None

    get_input_string() -> str

    show_string(input_string: str) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
def get_input_string() -> str:
    print('Enter words separated by a space:')
    input_string: str = input()
    return input_string


def show_string(input_string: str) -> None:
    for i, word in enumerate(input_string.split(' ')):
        print(f'{i + 1}: {word[:10]}')


def main() -> None:
    input_string: str = get_input_string()
    show_string(input_string)


if __name__ == '__main__':
    print(__doc__)
    main()
