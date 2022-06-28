#!/usr/bin/env python3
""">>>\nThis module demonstrate a worker personal data model using special
class and another class to process the information of this instance.

Classes:
    Worker
    Position(Worker)

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
# TODO: проверить значения атрибутов


class Worker:
    """This is a base class for a Worker object."""

    def __init__(self,
        name: str,
        surname: str,
        position: str,
        wage: int,
        bonus: int
    ) -> None:
        """Creates a Worker object with the specified external
        parameters like "name", "surname", "position", "wage" and "bonus".
        """
        self.name: str = name
        self.surname: str = surname
        self.position: str = position
        self._income: dict[str, int] = {
            "wage": wage,
            "bonus": bonus
        }

    def __str__(self):
        pass


class Position(Worker):
    """This is a child-class of Worker parent class.
    It uses to process the information of instance of Worker class.
    """

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self) -> str:
        """The method concatenates the first and last employee's names
        separated by a space.

        Returns:
            string with the full name of the employee.
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> int:
        """The method calculates the full employee's income.

        Returns:
            total employee's income including bonuses
        """
        return sum(self._income.values())


def main() -> None:
    """The execution point for the program file."""
    name: str = 'Eugene'
    surname: str = 'Nemykin'
    position: str = 'python developer'
    wage: int = 100_000
    bonus: int = 10_000
    new_worker_obj = Position(name, surname, position, wage, bonus)
    print(f'New worker: {new_worker_obj.get_full_name()}')
    print(f'\ttotal income: {new_worker_obj.get_total_income()} RUB')


if __name__ == '__main__':
    print(__doc__)
    main()
