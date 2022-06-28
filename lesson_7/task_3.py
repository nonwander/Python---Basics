#!/usr/bin/env python3
""">>>\nThis module demonstrates an actions that can be applied to a class
of an organic cell consisting of elementary particles.
Don't using special NumPy library for operations.

Classes:
    Cell

Exceptions:
    TypeError
    ValueError

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
# TODO: Fix tests using "assert".
# TODO: Refactoring to make all DRY.
from typing import Optional


class Cell:
    """The class of organic cell consisting of elementary particles.
    """
    def __init__(self, particle: int) -> None:
        """Creates a Cell object with the size parameter as argument.

        Arguments:
            particle -- the value of elementary particles.
        """
        self.particle: int = particle

    @property
    def particle(self) -> int:
        """Get or set the current value for Cell's particle.
        New value will valideted by type of instance and range of value.

        Arguments:
            particle -- value of cell's elementary particles in integer.

        Raises:
            ValueError: raises if value is not in available range;
            TypeError: raises if entered value is not integer type.

        Returns:
            _description_
        """
        return self._particle

    @particle.setter
    def particle(self, particle: int) -> int:
        err_msg: str = 'entered value must be positive integer!'
        if isinstance(particle, int):
            if particle > 0:
                self._particle: int = particle
                return self.particle
            else:
                raise ValueError(err_msg)
        else:
            raise TypeError(err_msg)

    def __add__(self, other: 'Cell') -> Optional['Cell']:
        """Union of two Cells.

        Returns:
            sum of the particles of the original two cells.
        """
        if self.validate_cells(other):
            result: int = self.particle + other.particle
            return Cell(result)

    def __sub__(self, other: 'Cell') -> Optional['Cell']:
        """Subtraction of two Cells.
        Operation performed only if the number of self particles
        is greater than the number of other Cell's particles.

        Returns:
            subtraction of the particles of the original two cells.
        """
        if self.validate_cells(other):
            result: int = self.particle - other.particle
            try:
                if result > 0:
                    return Cell(result)
                else:
                    raise ValueError('Subtraction is below zero!')
            except ValueError as err:
                print(f'Error: {err}')
                return None

    def __mul__(self, other: 'Cell') -> Optional['Cell']:
        """Multiplication of two Cells.

        Returns:
            product of the particles of the original two cells.
        """
        if self.validate_cells(other):
            result: int = self.particle * other.particle
            return Cell(result)

    def __truediv__(self, other: 'Cell') -> Optional['Cell']:
        """Division of two Cells.

        Returns:
            integer division of the particles of the original two cells.
        """
        if self.validate_cells(other):
            result: int = round(self.particle / self.particle)
            return Cell(result)

    def __str__(self) -> str:
        """Represents a Cell object as its particles contents.

        Returns:
            a string of all the particles of the current Cell.
        """
        return f'({self.particle * "*"})'

    def validate_cells(self, other) -> bool:
        """Checks whether instances match the Cell type.

        Arguments:
            other -- second instance of Cell type.

        Raises:
            TypeError: raises if instance is not of Cell type.

        Returns:
            boolean value that depends of validation result.
        """
        err_msg: str = 'invalid type of the instance cell!'
        try:
            if isinstance(other, self.__class__):
                return True
            else:
                raise TypeError(err_msg)
        except TypeError as err:
            print(f'Error: {err}')
            return False

    @classmethod
    def make_order(cls,
        cell_object: 'Cell',
        particle_in_row: int
    ) -> Optional[str]:
        """Represents Cell's particles in rows. Accepts an instance of the
        Cell class and the number of particles in a row.

        Arguments:
            cell_object -- instance of the class Cell;
            particle_in_row -- number of particles in a row.

        Raises:
            TypeError: raises if entered value of argument "particle_in_row"
                       is not integer type;
            TypeError: raises if cell_object is not Cell type.

        Returns:
            a string of a special form in which all the particles
            of the cell are divided into rows according to the number
            specified in the argument.
        """
        err_msg_part: str = 'entered value must be positive integer!'
        err_msg_cell: str = 'invalid type of the instance cell!'
        try:
            if cls.__instancecheck__(cell_object):
                if isinstance(particle_in_row, int):
                    cell_len: int = cell_object.particle
                    particle_in_line: str = '*' * cell_object.particle
                    order: list[str] = [
                        particle_in_line[idx:idx + particle_in_row]
                        for idx in range(0, cell_len, particle_in_row)
                    ]
                    return '\n'.join(order)
                else:
                    raise TypeError(f'"{particle_in_row}" - {err_msg_part}')
            else:
                raise TypeError(f'"{cell_object}" - {err_msg_cell}')
        except TypeError as err:
            print(f'Error: {err}')
            return None


def test_module() -> None:
    """Testing the Module with output to the console."""
    print('Initialize cells:')
    cell_1 = Cell(1)
    cell_2 = Cell(2)
    cell_3 = Cell(3)
    cell_16 = Cell(16)
    print(cell_1)
    print(cell_2)
    print(cell_3)
    print(cell_16)
    print('\nArythmetic with cells:')
    print(f'add: {cell_1} + {cell_2} = {cell_1 + cell_2}')
    print(f'sub: {cell_2} - {cell_1} = {cell_2 - cell_1}')
    print(f'mul: {cell_1} * {cell_2} = {cell_1 * cell_2}')
    print(f'div: {cell_3} / {cell_2} = {cell_3 / cell_2}')
    print(f'\nOrder to Cell with {cell_16.particle} particle:')
    print(Cell.make_order(cell_16, 5))
    print('\nIncorect actions with errors:')
    print(f'sub: {cell_1} - {cell_2} = {cell_1 - cell_2}')
    print(f'div: {cell_1} / {2} = {cell_1 / 2}')
    print(Cell.make_order(4, 5))
    print(Cell.make_order(cell_16, 'five'))
    # cell_4 = Cell(0)  # this must terminate program


def main() -> None:
    """The execution point for the program file."""
    test_module()


if __name__ == '__main__':
    print(__doc__)
    main()
