#!/usr/bin/env python3
""">>>\nThis module demonstrates inheritance of classes using
the example of the Stationery class.

Classes:
    Stationery

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
class Stationery:
    """This is a base class for a Stationery object."""
    def __init__(self, title: str) -> None:
        """Creates a Stationery object with the unique title.

        Arguments:
            title -- the name of the current Stationery object
        """
        self.title: str = title

    def __str__(self):
        return f'It is a {self.title}'

    def draw(self) -> str:
        return f'starting rendering'


class Pen(Stationery):
    """This is a child-class of Stationery parent class.
    """
    def draw(self) -> str:
        """Outputs a unique message that drawing is started
        by current Pen.

        Returns:
            message -- string about the beginning of drawing with a pen
        """
        message: str = f'{self.title} is {super().draw()} in the copybook'
        return message


class Pencil(Stationery):
    """This is a child-class of Stationery parent class.
    """
    def draw(self) -> str:
        """Outputs a unique message that drawing is started
        by current Pencil.

        Returns:
            message -- string about the beginning of drawing with a pencil
        """
        message: str = f'{self.title} is {super().draw()} in the album.'
        return message


class Handle(Stationery):
    """This is a child-class of Stationery parent class.
    """
    def draw(self) -> str:
        """Outputs a unique message that drawing is started
        by current Handle.

        Returns:
            message -- string about the beginning of drawing with a handle
        """
        message: str = f'{self.title} is {super().draw()} on the tablet.'
        return message


def main() -> None:
    """The execution point for the program file."""
    stationeries = [
        Pen('Pen'),
        Pencil('Pencil'),
        Handle('Marker'),
    ]
    for item in stationeries:
        print(item)
        print(item.draw())


if __name__ == '__main__':
    print(__doc__)
    main()
