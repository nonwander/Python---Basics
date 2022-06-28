#!/usr/bin/env python3
""">>>\nThis module demonstrates a custom class of a two-dimensional
matrix with built-in initialization and addition methods. If you execute it
two matrices of random numbers and one matrix as a result of their addition.
The User must first enter the dimension of the initial matrices.

NOTE: The solution does not use special NumPy library for operations.

Classes:
    Matrix

Exceptions:
    IndexError -- raises by the method if the input matrices
                  have different dimensions.

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
import random

from typing import NewType

RANDOM_NUM_RANGE = 10

TMatrix = NewType('TMatrix', list[list[int]])


class Matrix:
    """This is the class of two-dimensional matrix of integer numbers."""
    def __init__(self, matrix: list) -> None:
        """Creates a two-dimensional matrix object from a list with nested
        lists of element values.

        Arguments:
            matrix -- two-dimensional matrix
        """
        self.matrix = matrix

    def __add__(self, other: 'Matrix') -> TMatrix:
        """Sums two matrices of equal dimensions
        and identical type as 'Matrix'.

        Arguments:
            self -- the first required argument as matrix;
            other -- the second required argument as matrix.

        Returns:
            the new matrix type of Matrix as a result of addition.
        """
        matrix_a: TMatrix = self.matrix
        matrix_b: TMatrix = other.matrix
        try:
            sum_a_b: list[list[int]] = [
                [a_elem + b_elem for a_elem, b_elem in zip(a_row, b_row)]
                for (a_row, b_row) in zip(matrix_a, matrix_b)
            ]
            return Matrix(sum_a_b)
        except IndexError:
            print('both matrices must have equal dimensions!')
            exit(1)

    def __str__(self) -> str:
        """Defines the readable format of a two-dimensional matrix from its
        representation as a list with nested lists of element values.

        Returns:
            a string object formatted with special characters of the
            end of the matrix string.
        """
        matrix_in_str = []
        for row in self.matrix:
            matrix_in_str.append('\t'.join([str(elem) for elem in row]))
        return '\n'.join(matrix_in_str)


def get_random_data(rows: int, cols: int, num_range: int) -> list[list[int]]:
    """Generate creates a list of lists with random elements values as initial
    data for a two-dimensional matrix according to the specified parameters
    of the matrix dimension and the range of random numbers.

    Arguments:
        rows -- number of matrix rows;
        cols -- number of matrix cols;
        num_range -- range of random numbers.

    Returns:
        list of lists of random elements integer type.
    """
    matrix: list[list[int]] = [
        [random.randint(0, num_range) for _ in range(cols)]
        for _ in range(rows)
    ]
    return matrix


def get_init_params() -> tuple[int, int]:
    """Asks the User to enter the initial data to create
    a two-dimensional matrix

    Returns:
        values of rows and cols of the matrix in tuple of integer.
    """
    print('\nEnter the dimension of the matrix separated by a space')
    print('<rows> <columns>: ')
    rows, cols = map(int, input('').split())
    return rows, cols


def main() -> None:
    """The execution point for the program file."""
    num_range: int = RANDOM_NUM_RANGE
    rows, cols = get_init_params()
    matrix_a: TMatrix = Matrix(get_random_data(rows, cols, num_range))
    print('\nInitial matrix A:')
    print(matrix_a)
    matrix_b: TMatrix = Matrix(get_random_data(rows, cols, num_range))
    print('\nInitial matrix B:')
    print(matrix_b)
    matrix_c: TMatrix = matrix_a + matrix_b
    print('\nResulting sum matrix C = A + B:')
    print(matrix_c)


if __name__ == '__main__':
    print(__doc__)
    main()
