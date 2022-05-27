#!/usr/bin/env python3
""">>>\nThis module converts the time from seconds to %s format.

Functions:

    main() -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_input_time_sec() -> int

    get_converted_time(input_time_sec: int) -> dict

    show_time(input_time: dict) -> None

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""


from typing import Any, Callable

FORMAT = r'"{hh}:{mm}:{ss}"'


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
def get_input_time_sec() -> int:
    input_data: str = input('Enter time in seconds using natural integer: ')
    time_sec = int(input_data)
    if time_sec <= 0:
        raise ValueError(
            'entered number is out of range, must be a positive integer!'
        )
    return time_sec


def get_converted_time(input_time_sec: int) -> dict:
    time = input_time_sec
    time_in_dict = {
        'hh': 0,
        'mm': 0,
        'ss': 0,
    }
    seconds = time % 60
    hours = time // 3600
    minutes = ((time - seconds) // 60) - (hours * 60)
    time_in_dict['hh'] = hours
    time_in_dict['mm'] = minutes
    time_in_dict['ss'] = seconds
    return time_in_dict


def show_time(input_time: dict) -> None:
    print((FORMAT.format(**input_time)))


def main() -> None:
    input_time_sec: str = get_input_time_sec()
    converted_time: dict = get_converted_time(input_time_sec)
    show_time(converted_time)


if __name__ == '__main__':
    __doc__ %= FORMAT
    print(__doc__)
    main()
