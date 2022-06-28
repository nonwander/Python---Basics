#!/usr/bin/env python3
""">>>\nThis module presents the project "Office equipment Warehouse".

Classes:
    OfficeEquipment

Exceptions:

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
# TODO: Create Mixin for argument "supported_format"
# TODO: For a large amount of data it is better to create
#       custom dictionary class - this way data processing will be
#       faster and take up less memory.
# TODO: For all special methods like "start_copy", "start_scan", "start_print"
#       are need to create some logic, which will switching the boolean
#       result value.
from itertools import count as itcount
from typing import Any, Callable, Union


class Warehouse:
    """This is the container class of storage in a warehouse.
    """
    def __init__(self):
        """Create the instance of admission into the database "Warehouse".
        """
        self._dict: dict[str, OfficeEquipment] = {}

    def __str__(self):
        """String representation of element in Warehouse.

        Returns:
            group title of Equipment instance in Warehouse.
        """
        return f'{self._dict.keys()}'

    def reception(self, equipment: 'OfficeEquipment'):
        """Reception of office equipment at the warehouse.

        Arguments:
            equipment -- instance of any OfficeEquipment type.
        """
        try:
            if isinstance(equipment, OfficeEquipment):
                quantity: int = int(input('Введите количество: '))
                for _ in range(quantity):
                    object: 'OfficeEquipment' = equipment.create()
                    self._dict.setdefault(equipment.group, []).append(object)
            else:
                raise TypeError(
                    'instance must be of any OfficeEquipment type!'
                )
        except TypeError as err:
            print(f'Error: {err}')

    def extract(self, equipment: 'OfficeEquipment'):
        """Transfer to a specific division of the company.

        Arguments:
            equipment -- instance of any OfficeEquipment type.
        """
        # TODO: extraction works only with all group, but it will be
        # better to enter certain for extracting.
        try:
            if isinstance(equipment, OfficeEquipment):
                if self._dict[equipment.group]:
                    print(
                        f'Transfer {len(self._dict[equipment.group])} '
                        f'of {equipment.group}'
                    )
                    return self._dict.pop(equipment.group)
            else:
                raise TypeError(
                    'instance must be of any OfficeEquipment type!'
                )
        except TypeError as err:
            print(f'Error: {err}')


class OfficeEquipment():
    """This is the base class of Office Equipment.
    """
    __inventory_num: int = itcount(1)
    _ALLOWED_FORMAT_LIST: list[str] = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']

    def __init__(
        self, name: str, price: int, year: int, supported_format: str,
        **kwargs
    ) -> None:
        """Creates the instance of OfficeEquipment class.

        Arguments:
            name -- name or title of equipment;
            price -- equipment price in RUB;
            year -- production or reception year;
            supported_format -- supported paper format for current equipment.
        """
        self.id: int = next(OfficeEquipment.__inventory_num)
        self.group: str = self.__class__.__name__
        self.name: str = name
        self.price: int = price
        self.date: int = year
        self.supported_format: str = supported_format
        super().__init__(**kwargs)

    def __str__(self) -> str:
        """Represents group, id, name and parameters of the object.
        """
        return (
            f'\n{self.group} {self.name}, inventory №{self.id}'
            f'\n\tprice: {self.price} RUB\n\tyear: {self.date}'
        )

    @property
    def supported_format(self) -> int:
        """Get or set the current supported format of paper.
        New value is valideted by allowed format list written in constant.

        Arguments:
            supported_format -- supported paper format for current equipment.

        Raises:
            ValueError: raises if value is not in available range;
        """
        return self._supported_format

    @supported_format.setter
    def supported_format(self, supported_format: str) -> None:
        if supported_format in self._ALLOWED_FORMAT_LIST:
            self._supported_format: str = supported_format
        else:
            raise ValueError('wrong format value!')

    def validate_input(function) -> Callable[[], Any]:
        """Decorator for validating an incoming function.

        Arguments:
            function -- any incoming function.

        Returns:
            function -- validated function that returns an error-free result.
        """
        def _validator(*args, **kwargs) -> Any:
            """Wrapper function that monitors the ValueError.
            If the function being decorated fails, the wrapper
            function calls it again until it succeeds.

            Returns:
                result -- the result value of executing the decorated function.

            Exceptions:
                ValueError
            """
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

    @classmethod
    @validate_input
    def _new_data(cls) -> dict[str, Union[bool, int, str]]:
        """Requests data from the user to initialize an instance of the class.

        Returns:
            data -- dictionary with the values of the parameters
                of the future instance.
        """
        data: dict[str, Union[bool, int, str]] = {}
        data['name']: str = input('Enter item name: ')
        data['price']: int = int(input('Enter item price (RUB): '))
        data['year']: int = int(input('Enter production year : '))
        print(f'Allowed formats: {cls._ALLOWED_FORMAT_LIST}')
        data['supported_format']: str = input('Enter supported paper format: ')
        return data


class Printer(OfficeEquipment):
    """This is the class of Printer."""
    _PRINTING_TECH_DICT: dict[int, str] = {1: 'laser', 2: 'inkjet'}
    _COLOR_DICT: dict[int, bool] = {1: True, 0: False}

    def __init__(self, name: str, price: int, year: int,
        supported_format: list[str], is_colored: int, printing_tech: int,
        **kwargs
    ):
        """Creates the instance of Printer class.

        Arguments:
            name -- name or title of equipment;
            price -- equipment price in RUB;
            year -- production or reception year;
            supported_format -- supported paper format for current equipment.
        """
        super().__init__(name, price, year, supported_format,
        **kwargs
        )
        self.printing_tech: str = printing_tech
        self.is_colored: bool = is_colored

    @property
    def is_colored(self) -> bool:
        """Get or set the current supported coloring.
        New value is valideted by allowed variants written in constant.

        Arguments:
            is_colored -- bolean parameter for coloring printing.

        Raises:
            ValueError: raises if value is not in available variants.
        """
        return self._is_colored

    @is_colored.setter
    def is_colored(self, is_colored: int) -> None:
        if is_colored in self._COLOR_DICT:
            self._is_colored: bool = self._COLOR_DICT[is_colored]
        else:
            raise ValueError('wrong value of type!')

    @property
    def printing_tech(self) -> str:
        """Get or set the supported printing technology.
        New value is valideted by allowed variants written in constant.

        Arguments:
            printing_tech -- printing technology used by current equipment.

        Raises:
            ValueError: raises if value is not in available variants.
        """
        return self._printing_tech

    @printing_tech.setter
    def printing_tech(self, printing_tech: int) -> None:
        if printing_tech in self._PRINTING_TECH_DICT:
            self._printing_tech: str = self._PRINTING_TECH_DICT[printing_tech]
        else:
            raise ValueError('wrong value of type!')

    @classmethod
    @OfficeEquipment.validate_input
    def _new_data(cls) -> dict[str, Union[bool, int, str]]:
        """Requests data from the user to initialize an instance of the class.

        Returns:
            data -- dictionary with the values of the parameters
                of the future instance.
        """
        data: dict[str, Union[bool, int, str]] = super()._new_data()
        print(f'Allowed coloring: {cls._COLOR_DICT}')
        data['is_colored']: int = int(
            input('Enter is coloring allowed for printing: ')
        )
        print(f'Allowed tech: {cls._PRINTING_TECH_DICT}')
        data['printing_tech'] = int(
            input('Enter what printing technology is used: ')
        )
        return data

    @classmethod
    @OfficeEquipment.validate_input
    def create(cls) -> 'Printer':
        """Creates the instance of Printer class from User validated input.

        Returns:
            instance of Printer class.
        """
        print(f'\n*** Creating data of new {cls.__name__} ***')
        data: dict[str, Union[bool, int, str]] = super()._new_data()
        name: str = data['name']
        price: int = data['price']
        year: int = data['year']
        supported_format: str = data['supported_format']
        print(f'Allowed coloring: {cls._COLOR_DICT}')
        is_colored: int = int(
            input('Enter is coloring allowed for printing: ')
        )
        print(f'Allowed tech: {cls._PRINTING_TECH_DICT}')
        printing_tech: int = int(
            input('Enter what printing technology is used: ')
        )
        return Printer(
            name, price, year, supported_format,
            is_colored, printing_tech
        )

    def start_print(self) -> bool:
        """Special method for instance of Printer class.

        Returns:
            boolean value depending on the progress of the method operation.
        """
        print(
            f'Started printing: {self.supported_format} '
            f'{self.printing_tech}, color: {self.is_colored}')
        return True


class Scanner(OfficeEquipment):
    """This is the class of Scanner."""

    _RESOLUTION_DPI_LIST: list[int] = [100, 150, 200, 300, 600, 1200]

    def __init__(self, name: str, price: int, year: int,
        supported_format: str, scan_resolution_dpi: int,
        **kwargs
    ) -> None:
        """Creates the instance of Scanner class.

        Arguments:
            name -- name or title of equipment;
            price -- equipment price in RUB;
            year -- production or reception year;
            supported_format -- supported paper format for current equipment.
        """
        super(Scanner, self).__init__(
            name, price, year, supported_format,
            **kwargs,
        )
        self.scan_resolution_dpi: int = scan_resolution_dpi

    @property
    def scan_resolution_dpi(self) -> int:
        """Get or set the current supported scan resolution.
        New value will valideted by allowed values in constant list.

        Arguments:
            scan_resolution_dpi -- the amount of scanner detail in dots
                per inch (dpi).

        Raises:
            ValueError: raises if value is not in available variants.
        """
        return self._scan_resolution_dpi

    @scan_resolution_dpi.setter
    def scan_resolution_dpi(self, scan_resolution_dpi: int) -> None:
        if scan_resolution_dpi in self._RESOLUTION_DPI_LIST:
            self._scan_resolution_dpi: int = scan_resolution_dpi
        else:
            raise ValueError('wrong scan resolution value!')

    @classmethod
    @OfficeEquipment.validate_input
    def _new_data(cls) -> dict[str, Union[bool, int, str]]:
        """Requests data from the user to initialize an instance of the class.

        Returns:
            data -- dictionary with the values of the parameters
                of the future instance.
        """
        data: dict[str, Union[bool, int, str]] = super()._new_data()
        print('Allowed resolution in dots per inch (dpi): '
            f'{cls._RESOLUTION_DPI_LIST}'
        )
        data['scan_resolution_dpi']: int = int(
            input('Enter scan resolution in dpi: ')
        )
        return data

    @classmethod
    @OfficeEquipment.validate_input
    def create(cls) -> 'Scanner':
        """Creates the instance of Scanner class from User validated input.

        Returns:
            instance of Scanner class.
        """
        print(f'\n*** Creating data of new {cls.__name__} ***')
        data: dict[str, Union[bool, int, str]] = super()._new_data()
        name: str = data['name']
        price: int = data['price']
        year: int = data['year']
        supported_format: str = data['supported_format']
        print(
            'Allowed resolution in dots per inch (dpi): '
            f'{cls._RESOLUTION_DPI_LIST}'
        )
        scan_resolution_dpi: int = int(
            input('Enter scan resolution in dpi: ')
        )
        return Scanner(
            name, price, year, supported_format,
            scan_resolution_dpi
        )

    def start_scan(self) -> bool:
        """Special method for instance of Scanner class.

        Returns:
            boolean value depending on the progress of the method operation.
        """
        print(
            f'Started scaning: {self.supported_format} '
            f'with {self.scan_resolution_dpi} dpi.'
        )
        return True


class Xerox(Printer, Scanner):
    """This is the class of Xerox."""

    _COPY_SPEED_RANGE: int = 60

    def __init__(self, name: str, price: int, year: int,
        supported_format: str, is_colored: int, printing_tech: int,
        scan_resolution_dpi: int, xcopy_speed: int,
        **kwargs
    ) -> None:
        """Creates the instance of Xerox class.

        Arguments:
            name -- name or title of equipment;
            price -- equipment price in RUB;
            year -- production or reception year;
            supported_format -- supported paper format for current equipment.
        """
        super().__init__(name, price, year, supported_format,  # fom OfficeEquipment
            is_colored=is_colored, printing_tech=printing_tech,  # from Printer
            scan_resolution_dpi=scan_resolution_dpi,  # from Scanner
            **kwargs
        )
        self.xcopy_speed: int = xcopy_speed

    @property
    def xcopy_speed(self) -> int:
        """Get or set the current supported copy speed.
        New value will valideted by allowed range in class constant.

        Arguments:
            xcopy_speed -- value of pages number per min.

        Raises:
            ValueError: raises if value is not in available range.
        """
        return self._xcopy_speed

    @xcopy_speed.setter
    def xcopy_speed(self, xcopy_speed: int) -> None:
        if xcopy_speed in range(self._COPY_SPEED_RANGE + 1):
            self._xcopy_speed: int = xcopy_speed
        else:
            raise ValueError('incorrect copying speed value!')

    @classmethod
    @OfficeEquipment.validate_input
    def _new_data(cls) -> dict[str, Union[bool, int, str]]:
        """Requests data from the user to initialize an instance of the class.

        Returns:
            data -- dictionary with the values of the parameters
                of the future instance.
        """
        data: dict[str, Union[bool, int, str]] = super()._new_data()
        print(
            'Allowed copying speed range (1, '
            f'{cls._COPY_SPEED_RANGE})'
        )
        data['xcopy_speed']: int = int(
            input('Enter copying speed in pages per minutes: ')
        )
        return data

    @classmethod
    @OfficeEquipment.validate_input
    def create(cls) -> 'Xerox':
        """Creates the instance of Xerox class from User validated input.

        Returns:
            instance of Xerox class.
        """
        print(f'\n*** Creating data of new {cls.__name__} ***')
        data: dict[str, Union[bool, int, str]] = cls._new_data()
        name: str = data['name']
        price: int = data['price']
        year: int = data['year']
        supported_format: str = data['supported_format']
        is_colored: int = data['is_colored']
        printing_tech: int = data['printing_tech']
        scan_resolution_dpi: int = data['scan_resolution_dpi']
        xcopy_speed: int = data['xcopy_speed']
        return Xerox(
            name, price, year, supported_format,
            is_colored, printing_tech,
            scan_resolution_dpi, xcopy_speed
        )

    def start_copy(self) -> bool:
        """Special method for instance of Xerox class.

        Returns:
            boolean value depending on the progress of the method operation.
        """
        # TODO: add number of lists to copy, timing,
        # demonstrate progress at real time in console.
        print(f'Started copying at a speed of {self.xcopy_speed} pages/min')
        self.start_scan()
        self.start_print()
        return True


def test_module() -> None:
    """Testing the Module with output to the console."""
    printer = Printer('Hp', 15_000, 2022, 'A4', 1, 2)
    printer.start_print()
    scanner = Scanner('EPSON', 10_000, 2020, 'A4', 1_200)
    scanner.start_scan()
    xerox = Xerox('Brother', 30_000, 2010, 'A4', False, 1, 300, 16)
    xerox.start_copy()

    storage = Warehouse()
    storage.reception(xerox)
    for obj in storage.extract(xerox):
        print(obj)


def main() -> None:
    """The execution point for the program file."""
    test_module()


if __name__ == '__main__':
    print(__doc__)
    main()
