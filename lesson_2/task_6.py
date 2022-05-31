#!/usr/bin/env python3
""">>>\nThis module implements the "Products" data structure.
List elements can be entered by the user or readed from the file.
Also program have constant with Products to demonstrate.

Functions:

    main(command: str) -> None

    validate_input(function) -> Callable[[], Any]

    _validator(*args, **kwargs) -> Any

    get_number_product() -> int

    get_product() -> dict

    get_data_from_json() -> list[tuple[int, Any]]

    show_data(input_data: list[tuple[int, dict[str, Any]]]) -> None

    get_analytics(input_data: list[tuple]) -> None

    combine_dict(
        dict_1: dict[str, list],
        dict_2: dict[str, Any],
        keys: tuple[str]
    ) -> dict[str, list]:

Exceptions:
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
import json
from pprint import pprint
from typing import Any, Callable

INPUT_JSON = 'task_6.json'

PRODUCTS = [
    (1, {'name': 'computer', 'price': 20000, 'quantity': 5, 'units': 'pcs.'}),
    (2, {'name': 'printer', 'price': 6000, 'quantity': 2, 'units': 'pcs.'}),
    (3, {'name': 'scanner', 'price': 2000, 'quantity': 7, 'units': 'pcs.'})
]


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
def get_number_product() -> int:
    input_number: str = input('Enter the number of products: ')
    number_product = int(input_number)
    if number_product <= 0:
        raise ValueError(
            'entered number is out of range, must be a positive integer!'
        )
    return number_product


@validate_input
def get_product() -> dict:
    UNITS = {
        '1': 'pcs.',
        '2': 'm',
        '3': 'kg'
    }
    product: dict = dict()
    product['name'] = input('name: ')
    product['price'] = int(input('price: '))
    product['quantity'] = int(input('quantity: '))
    print('Enter: "1" - pcs., "2" - m, "3" - kg, or ignore for Nonetype')
    product['units'] = UNITS.get(
        input('units: ')
    )
    return product


def get_data_from_json() -> list[tuple[int, Any]]:
    data_products = list()
    with open(INPUT_JSON, 'r', encoding='utf-8') as file:
        data = json.load(file)
    for key, value in data.items():
        data_products.append((int(key), value))
    return data_products


def show_data(input_data: list[tuple[int, dict[str, Any]]]) -> None:
    print('\tProducts in database:')
    for idx in range(len(input_data)):
        print(input_data[idx])


def get_analytics(input_data: list[tuple]) -> None:

    def combine_dict(
        dict_1: dict[str, list],
        dict_2: dict[str, Any],
        keys: tuple[str]
    ) -> dict[str, list]:
        return {
            key: (dict_1.get(key).append(dict_2.get(key))
            if dict_2.get(key) not in dict_1.get(key)
            else False)
            for key in keys
        }

    output_dict: dict = dict()
    keys = list()
    for idx in range(len(input_data)):
        keys += input_data[idx][1].keys()
    keys = tuple(set(keys))
    for key in keys:
        output_dict.update({key: []})
    for idx in range(len(input_data)):
        combine_dict(output_dict, input_data[idx][1], keys)
    pprint(output_dict)


def main(command: str) -> None:
    data_products: list[tuple] = list()
    if command == 'm':
        number_products: int = get_number_product()
        for idx in range(number_products):
            print(f'\tProduct №{idx + 1}:')
            input_product: dict = get_product()
            data_products.append((idx + 1, input_product))
    elif command == 'a':
        data_products: list[tuple] = PRODUCTS
    elif command == 'f':
        data_products: list[tuple] = get_data_from_json()
    show_data(data_products)
    get_analytics(data_products)


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
