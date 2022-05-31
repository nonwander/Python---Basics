#!/usr/bin/env python3
""">>>\nThis module swaps the values of neighboring list elements.
\nThe User needs to enter the values of the list elements.

Functions:

    main() -> None

    get_input_list() -> list[str]

    get_modified_list(input_list: list[str]) -> list[str]

    show_list(input_list: list[str]) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
def get_input_list() -> list[str]:
    input_list: list[str] = input(
        'Enter elements separated by a space: '
    ).split(' ')
    return input_list


def get_modified_list(input_list: list[str]) -> list[str]:
    for i in range(0, len(input_list) - 1, 2):
        input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
    return input_list


def show_list(input_list: list[str]) -> None:
    print(input_list)


def main() -> None:
    input_list: list[str] = get_input_list()
    modified_list: list[str] = get_modified_list(input_list)
    show_list(modified_list)


if __name__ == '__main__':
    print(__doc__)
    main()
