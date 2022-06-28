#!/usr/bin/env python3
""">>>\nThis method demonstrates the use of an abstract class as a parent
for the successor classes using the example of the Clothing class for
the Coat and Suit classes.

Classes:
    Clothes(ABC)
    Coat(Clothes)
    Suit(Clothes)

Exceptions:
    ValueError
    TypeError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    """This is the abstract class of Clothes.

    Arguments:
        ABC -- helper class that provides a standard way to create
            an abstract base class using inheritance.
    """
    def __init__(self, name: str) -> None:
        """Creates a certain type of clothing.

        Arguments:
            name -- name of clothing.
        """
        self.name: str = name

    @abstractmethod
    def fabric_consumption_m(self) -> float:
        """Calculates the consumption of fabric by type of clothing.

        Returns:
            fabric_m -- fabric consumption in meters.
        """
        pass


class Coat(Clothes):
    """This is the child-class of Clothes named Coat type.

    Arguments:
        Clothes -- the parent abstract base class.
    """
    _size_min: int = 38
    _size_max: int = 86

    def __init__(self, name: str, size: int) -> None:
        """Creates a Coat object with the size parameter as argument.

        Arguments:
            name -- the name of new Coat object;
            size -- the value of size parameter.
        """
        super().__init__(name)
        self.size: int = size

    def __str__(self) -> str:
        """Represents name, parameters and fabric consumption of the object.
        """
        return (
            f'{self.__class__.__name__}:  "{self.name}", '
            f'size: {self.size}.'
            f'\n\tFabric consumption: {self.fabric_consumption_m} m.'
        )

    @property
    def size(self) -> int:
        """Get or set the current value for clothes size.
        New value will valideted by type of instance and range of value.

        Arguments:
            size -- value of clothes size.

        Raises:
            ValueError: raises if value is not in available range;
            TypeError: raises if entered value is not integer type.
        """
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        if isinstance(size, int):
            if size in range(self._size_min, self._size_max + 1):
                self._size = size
            else:
                raise ValueError('wrong range of size value!')
        else:
            raise TypeError('entered value must be positive integer!')

    @property
    def fabric_consumption_m(self) -> float:
        """Calculates the fabric consumption of the object.

        Returns:
            fabric_m -- value of fabric consumption in meters.
        """
        fabric_m: float = self.size / 6.5 + 0.5
        return round(fabric_m, 2)


class Suit(Clothes):
    """This is the child-class of Clothes named Suit type.

    Arguments:
        Clothes -- the parent abstract base class.
    """
    _height_cm_max: int = 200
    _height_cm_min: int = 100

    def __init__(self, name: str, height_cm: int) -> None:
        """Creates a Suit object with the height parameter as argument.

        Arguments:
            name -- the name of new Suit object;
            height_cm -- the value of height parameter in cm.
        """
        super().__init__(name)
        self.height_cm: float = height_cm

    def __str__(self) -> str:
        """Represents name, parameters and fabric consumption of the object.
        """
        return (
            f'{self.__class__.__name__}:  "{self.name}", '
            f'height: {self.height_cm} cm.'
            f'\n\tFabric consumption: {self.fabric_consumption_m} m.'
        )

    @property
    def height_cm(self) -> int:
        """Get or set the current value of height parameter.
        New value will valideted by type of instance and range of value.

        Arguments:
            height_cm -- value of height parameter in cm.

        Raises:
            ValueError: raises if value is not in available range;
            TypeError: raises if entered value is not integer type.
        """
        return self._height_cm

    @height_cm.setter
    def height_cm(self, height_cm: int) -> None:
        if isinstance(height_cm, int):
            if height_cm in range(self._height_cm_min, self._height_cm_max + 1):
                self._height_cm = height_cm
            else:
                raise ValueError('wrong range of height value!')
        else:
            raise TypeError('entered value must be positive integer!')

    @property
    def fabric_consumption_m(self) -> float:
        """Calculates the fabric consumption of the object.

        Returns:
            fabric_m -- value of fabric consumption in meters.
        """
        fabric_m: float = 2 * (self.height_cm / 100) + 0.3
        return round(fabric_m, 2)


def test_module() -> None:
    """Testing the Module with output to the console."""
    coat: 'Coat' = Coat('Overcoat', 38)
    print(coat)
    suit: 'Suit' = Suit('Russian', 180)
    print(suit)


def main() -> None:
    """The execution point for the program file."""
    test_module()


if __name__ == '__main__':
    print(__doc__)
    main()
