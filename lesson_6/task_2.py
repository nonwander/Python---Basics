#!/usr/bin/env python3
""">>>\nThis module demonstrates calculating the mass of asphalt required
to cover the entire road determine in instance of Road class.

Using formula:
    length[m] * width[m] * thickness[cm] *
    * (mass of asphalt to cover 1 sq.m. of asphalt road and 1 cm thick)[kg]

Classes:
    Road

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
from functools import reduce


class Road:
    """This is a class for a roadway object.

    Constants:
        MASS_kg -- mass of asphalt to cover 1 sq.m. and 1 cm thick
            of asphalt road, is PRIVATE
    """
    __MASS_kg: int  = 25

    def __init__(self, length_m, width_m, thickness_cm) -> None:
        """Creates a Road object with the specified external
        parameters like length, width and thickness.

        Arguments:
            length_m -- length (m) of the roadway object, is PROTECTED;
            width_m -- width (m) of the roadway object, is PROTECTED;
            thickness_cm -- thickness (cm) of the roadway object.
        """
        self._length_m: int = length_m
        self._width_m: int = width_m
        self.thickness_cm: int = thickness_cm
    
    def __str__(self) -> str:
        """Shows all parameters and properties of the roadway object.

        Returns:
            string interpretation of all roadway parameters in formula type.
        """
        self.road_mass_kg: int = self.calculate_road_mass()
        roadway_presentation: str = (
            'Resulting mass of the roadway:\n'
            f'{self._length_m}m * '
            f'{self._width_m}m * '
            f'{self.__MASS_kg}kg * '
            f'{self.thickness_cm}cm = '
            f'{self.road_mass_kg // 1_000}t'
        )
        return roadway_presentation

    def calculate_road_mass(self) -> int:
        """Calculates the mass of the whole roadway object.

        Returns:
            result_road_mass_kg -- resulting mass of the road
                calculated by the special formula.
        """
        result_road_mass_kg: int = reduce((lambda x, y: x * y),
            [self._length_m, self._width_m, self.__MASS_kg, self.thickness_cm]
        )
        return result_road_mass_kg


def main() -> None:
    """The execution point for the program file."""
    length_m: int = 20
    width_m: int = 5_000
    thickness_cm: int = 5
    new_road_obj = Road(length_m, width_m, thickness_cm)
    print(new_road_obj)


if __name__ == '__main__':
    print(__doc__)
    main()
