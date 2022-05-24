#!/usr/bin/env python3
""">>>\nThis module helps to sort the elements by type
from the line entered by the user and separated by a space.

Functions:

    main() -> None

    get_input_data() -> str

    get_separated_data(input_data: str) -> dict

    show_separate_data(input_data: dict) -> None

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""


def get_input_data() -> str:
    data = input('Enter some numbers and strings separated by a space: ')
    if not data:
        print('It`s empty! Try again!')
        return(get_input_data())
    else:
        print('Good job!')
        return data


def get_separated_data(input_data: str) -> dict:
    data = input_data.split(' ')
    data_dict = {
        'chars': [],
        'numbers': [],
        'strings': [],
        'floats': []
    }
    for chunk in data:
        if chunk.isdigit():
            data_dict['numbers'].append(int(chunk))
        elif chunk.isalpha():
            data_dict['strings'].append(chunk)
        else:
            if chunk.count('.') == 1 and chunk[:1] != '.' and chunk[-1] != '.':
                try:
                    data_dict['floats'].append(float(chunk))
                except ValueError:
                    data_dict['chars'].append(chunk)
            else:
                data_dict['chars'].append(chunk)
    return data_dict


def show_separate_data(input_data: dict) -> None:
    for key, value in input_data.items():
        print(key, value)


def main() -> None:
    input_data: str = get_input_data()
    separate_data: dict = get_separated_data(input_data)
    show_separate_data(separate_data)


if __name__ == '__main__':
    print(__doc__)
    main()
