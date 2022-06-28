#!/usr/bin/env python3
""">>>\nThis module contains the class ComplexNumber class,
which allows you to create objects representing complex numbers
in Algebraic form. You can perform addition and multiplication
operations on objects of the class.

The algebraic form of the complex number 'z' is represented as:
z = a + bi,
where:
    Re(z) = a ∈ R
    Im(z) = b ∈ R

The sum of complex numbers (a + bi) and (c + di) is complex number:
(a + c + (b + d)i).

The product of complex numbers (a + bi) and (c + di) is complex number:
(a * c) - (b * d) + (a * d + b * c)i.

Classes:
    ComplexNumber

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
# TODO: implement the ability to perform mathematical operations
# of a ComplexNumber objects with a numbers of type int and float.


class ComplexNumber:
    """This is the custom class of complex number.
    """

    def __init__(self, real: float = 0, imag: float = 0) -> None:
        """Creates the instance of ComplexNumber class.

        Keyword Arguments:
            real -- the Real part of ComplexNumber (default: {0})
            imag -- the Imaginary part of ComplexNumber (default: {0})

        Raises:
            TypeError: raises if the first argument is not a number;
            TypeError: raises if the second argument is not a number.
        """
        if not isinstance(real, float | int):
            raise TypeError(
                f'first argument must be a number, not {type(real)}'
            )
        elif not isinstance(imag, float | int):
            raise TypeError(
                f'second argument must be a number, not {type(real)}'
            )
        else:
            self.real: float = real
            self.imag: float = imag

    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """The sum of complex numbers of ComplexNumber type.

        Arguments:
            other -- second summand of ComplexNumber type.

        Returns:
            ComplexNumber = (Re(self) + Re(other)) + (Im(self) + Im(other))
        """
        re: float = self.real + other.real
        im: float = self.imag + other.imag
        return ComplexNumber(re, im)

    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        """The product of two complex numbers of ComplexNumber type.

        Arguments:
            other -- second multiplier of ComplexNumber type.

        Returns:
            ComplexNumber = (Re(self) * Re(other)) - (Im(self) * Im(other)) +
                + (Re(self) * Im(other) + Im(self) * Re(other)).
        """
        re: float = self.real * other.real - self.imag * other.imag
        im: float = self.real * other.imag + self.imag * other.real
        return ComplexNumber(re, im)

    def __str__(self) -> str:
        """String representation of ComplexNumber.
        + if Reel part = 0, then it remains empty;
        + if Imaginary part = 0, then it remains empty;
        + if Imaginary part = 1, then it remains as "i"

        Returns:
            "(a + bi)", where "a" and "b" are real numbers,
            i - Imaginary unit.
        """
        im: str
        re: str
        if self.imag == 0:
            im = ''
        elif self.imag == 1:
            im = f'{"+i" if self.real else "i"}'
        else:
            im = f'{"+" if self.real else ""}{self.imag}i'
        if self.real == 0:
            re = f'{"" if self.imag else "0"}'
        else:
            re = f'{self.real}'
        return f'({re}{im})'

    def __repr__(self) -> str:
        re = f'{self.real}'
        im = f'{"+" if self.imag > 0 else ""}{self.imag}i'
        return f'{re}{im}'


def test_module():
    """Testing the Module with output to the console."""
    # TODO: Organize the output in a clear and readable form.
    SPLIT_LINE: str = '\n' + '*' * 79
    z0 = ComplexNumber()
    z00 = ComplexNumber(0, 0)
    z01 = ComplexNumber(0, 1)
    z11 = ComplexNumber(-1, -1)
    z22 = ComplexNumber(2, 2)
    z10 = ComplexNumber(1, 0)
    z6 = ComplexNumber(0, -10)
    print(SPLIT_LINE)
    print('My ComplexNumber class:')
    print(z0)
    print(z00)
    print(z01)
    print(z11)
    print(z10)
    print(SPLIT_LINE)
    print('My ComplexNumber multiplication:')
    print(z22 * z22)
    print(z22 * z6)
    print(z01 * z01)
    print(SPLIT_LINE)
    print('Checking with the built-in python class:')
    print(complex(2, 2) * complex(10, -10))
    print(complex())
    print(complex(0, 1) * complex(0, 1))
    print(repr(z6))
    print(SPLIT_LINE)
    print(
        'Compare results with the built-in python',
        'class for operations with numbers:'
    )
    print(complex(0, 1) + 2j)
    print(z01 + 2j)
    print(complex(0, 1) + 2)
    print(z01 + 2)


def main() -> None:
    """The execution point for the program file."""
    test_module()


if __name__ == '__main__':
    print(__doc__)
    main()
