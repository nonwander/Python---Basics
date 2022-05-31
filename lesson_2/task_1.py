#!/usr/bin/env python3
""">>>\nThis module check the type of the list elements.
List elements can be entered by the User or readed from the file.
Also program have constant with elements and types to demonstrate.
\nThe 'type()' function is used for the solution.

Functions:

    main(command: str) -> None

    get_input_data() -> list[str]

    get_typed_dict(input_data: str) -> dict[str, Any]

    show_typed_dict(input_data: dict[str, Any]) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from typing import Any

PYTHON_TYPES = {
    'None': None,
    'True': True,
    'False': False,
    '256': 256,
    '0b11111111': 0b11111111,
    '0xFF': 0xFF,
    '0o11': 0o11,
    '0.256': 0.256,
    '2.5 + 6j': 2.5 + 6j,
    '(2, 5, 6)': (2, 5, 6),
    '[2, 5, 6]': [2, 5, 6],
    '{2, 5, 6}': {2, 5, 6},
    '{2: 2, 5: 5, 6: 6}': {2: 2, 5: 5, 6: 6},
    'range(0, 256)': range(0, 256),
    'string': 'string',
    r"b'\x00\x10\x02\x03'": b'\x00\x10\x02\x03',
    "b'2dLH'": b'2dLH'
}


def get_input_data() -> list[str]:
    data = input('Enter some numbers and strings separated by a space: ')
    if not data:
        print('It`s empty! Try again!')
        return(get_input_data())
    else:
        print('Good job!')
        return data.split(' ')


# TODO: Add other type checks like 'tuple', 'lits', 'set' etc.
def get_typed_dict(input_data: str) -> dict[str, Any]:
    result: dict[str, Any] = dict()
    for chunk in input_data:
        if chunk == 'None':
            typed_chunk = None
        elif chunk == 'True':
            typed_chunk = True
        elif chunk == 'False':
            typed_chunk = False
        elif chunk.isdigit():
            typed_chunk = int(chunk)
        elif chunk.count('+') == 1 and chunk[-1] == 'j':
            try:
                typed_chunk = complex(chunk)
            except ValueError:
                pass
        elif chunk.count('.') == 1 and chunk[:1] != '.' and chunk[-1] != '.':
            try:
                typed_chunk = float(chunk)
            except ValueError:
                pass
        elif chunk[:2] == '0x':
            try:
                typed_chunk = int(chunk, 16)
            except ValueError:
                pass
        elif chunk[:2] == '0b':
            try:
                typed_chunk = int(chunk, 2)
            except ValueError:
                pass
        elif chunk[:2] == '0o':
            try:
                typed_chunk = int(chunk, 8)
            except ValueError:
                pass
        # TODO: it would be more correct to check whether the ASCII value
        # of each character in 'chunk' is within desired ranges.
        elif chunk[:2] == "b'" and chunk[-1] == "'":
            try:
                typed_chunk = bytes(chunk.split("'")[1].encode('utf-8'))
            except ValueError:
                pass
        else:
            typed_chunk = chunk
        result.update({chunk: typed_chunk})
    return result


def show_typed_dict(input_data: dict[str, Any]) -> None:
    for key, value in input_data.items():
        print(f'{key} - is belongs to the type {type(value)}')


def main(command: str) -> None:
    if command == 'm':
        input_data: list[str] = get_input_data()
        typed_dict: dict[str, Any] = get_typed_dict(input_data)
    elif command == 'a':
        typed_dict: dict[str, Any] = PYTHON_TYPES
    elif command == 'f':
        with open('task_1.txt', 'r') as file:
            input_data: list[str] = file.read().splitlines()
        typed_dict: dict[str, Any] = get_typed_dict(input_data)
    show_typed_dict(typed_dict)


if __name__ == '__main__':
    print(__doc__)
    print(
        'Select variant for list elements generation:'
        '\n\tm - to create your own list'
        '\n\ta - to use program list'
        '\n\tf - to use external file'
    )
    while True:
        try:
            command: str = input('Type command: ')
            if command in ('m', 'a', 'f'):
                break
            else:
                print('Incorrect input!')
        except ValueError:
            pass
    main(command)
