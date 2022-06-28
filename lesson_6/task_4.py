#!/usr/bin/env python3
""">>>\nThis module demonstrate car driving using special methods
to get contol upon the instances of Car classes.

Classes:
    Car
    TownCar(Car)
    SportCar(Car)
    WorkCar(Car)
    PoliceCar(Car)

Exceptions:

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
import json
import time

from itertools import count as itcount
from random import choice as rand_ch


def axeleration(max_speed_kmh, speed_range_kmh, start_flag):
        def outer_wrapper(function):
            def wrapper(*args, **kwargs) -> bool:
                while True:
                    if start_flag == False:
                        return False
                    length = max_speed_kmh // 10
                    for current_speed_kmh in range(speed_range_kmh + 1):  # max_speed):
                        axel = f'[0 {(current_speed_kmh // 10) * "■"}'
                        axel += f'{(length - (current_speed_kmh // 10)) * "○"}'
                        axel += f' {max_speed_kmh} ] '
                        print(
                            f'{axel} {current_speed_kmh}'
                            f'{function(current_speed_kmh)}', end="\r"
                        )
                        time.sleep(0.05)
                    print(axel)
                    return False  # function(*args, **kwargs)
            return wrapper
        return outer_wrapper


class Car:
    """This is a base class for a Car object."""
    __id = itcount(1)
    _speed_limit_kmh = 120

    def __init__(self,
        speed: int, 
        color: str,
        name: str,
        is_police:
        bool = None
    ) -> None:
        """Creates a Car object with the specified external
        parameters like "name", "speed", "color", "is_police".
        """
        self.id: int = next(Car.__id)
        self._start_flag: bool = False
        self.name: str = name
        self.color: str = color
        self.speed_kmh: int = speed
        if is_police is None:
            self.is_police = False
        else:
            self.is_police = is_police
        self.speed_range = Car._speed_limit_kmh + 20
        #self.show_speed = axeleration(speed, self.speed_range)(self.show_speed)

    def __str__(self):
        car = {
            'Car id': self.id,
            'name': self.name,
            'color': self.color,
            'speed': self.speed_kmh,
            'direction': self.turn(),
            'police': self.is_police
        }
        return json.dumps(car)

    def _get_start(self):
        return self._start_flag
    
    def _set_start(self):
        self._start_flag = True

    def _del_start(self):
        self._start_flag = False

    def get_direction(self) -> str:
        # TODO: fix - return value only if start==True
        return rand_ch(['left', 'right', 'forward', 'backward'])

    def turn(self):
        if self._start_flag:
            return self.get_direction()
        return None

    def go(self):
        print(f'>>> {self.name} started!')
        self._set_start()
        return self._start_flag

    def stop(self):
        print(f'>>> {self.name} stopped!')
        self._del_start()
        return self._start_flag

    def show_speed(self, current_speed=0):
        if not self._start_flag:
            return '0 km/h'
        return f' km/h'

    start_flag = property(
        fget=_get_start,
        fset=_set_start,
        fdel=_del_start,
        doc='The start flag.'
    )


class TownCar(Car):
    """This is a class of simple town car.
    """
    _speed_limit_kmh: int = 60

    def __init__(self,
        speed: int,
        color: str,
        name: str,
        is_police: bool = None
    ) -> None:
        self._start_flag: bool = False
        self.speed_kmh: int = speed
        self.speed_range: int = TownCar._speed_limit_kmh + 20
        self.show_speed: str = axeleration(speed, self.speed_range, self._start_flag)(self.show_speed)
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed=0) -> str:
        if self._start_flag == False:
            return '0 km/h'
        speed_excess = current_speed - self._speed_limit_kmh + 1
        if 0 < speed_excess < self.speed_range:
            return(f' exceeding the speed limit by {speed_excess} km/h!')
        elif speed_excess >= self.speed_range:
            return(
                f' RECEIVED A FINE! Speeding more than 20 km/h '
                f'- CALLING POLICE!'
            )
        elif speed_excess <= 0:
            return f' km/h'


class WorkCar(Car):
    """This is a class of simple work car.
    """
    _speed_limit_kmh: int = 40

    def __init__(self,
        speed: int,
        color: str,
        name: str,
        is_police:
        bool = None
    ) -> None:
        self._start_flag: bool = False
        self.speed: int = speed
        self.speed_range: int = WorkCar._speed_limit_kmh + 20
        self.show_speed: str = axeleration(speed, self.speed_range, self._start_flag)(self.show_speed)
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed=0) -> str:
        if self._start_flag == False:
            return '0 km/h'
        speed_excess = current_speed - self._speed_limit_kmh
        if 0 < speed_excess < self.speed_range:
            return(f' exceeding the speed limit by {speed_excess} km/h!')
        elif speed_excess >= self.speed_range:
            return(f' FINE! Speeding more than 20 km/h - CALLING POLICE!')
        elif speed_excess <= 0:
            return f' km/h'


class SportCar(Car):
    """This is a class of simple sportcar.
    But nothing special for it.
    """
    pass


class PoliceCar(Car):
    """This is a class of simple police car.
    """
    def __init__(self,
        speed: int,
        color: str,
        name: str,
        is_police: bool = None
    ) -> None:
        is_police: bool = True
        super().__init__(speed, color, name, is_police)
        

def main() -> None:
    """The execution point for the program file."""
    name: str = 'Car'
    color: str = 'White'
    is_police: bool = False
    speed_kmh: int = 100

    car_fleet = [
        SportCar(240, 'red', 'Lamborghini'),
        TownCar(180, 'baklazhan', 'Lada'),
        WorkCar(140, 'orange', 'Kamaz'),
        PoliceCar(170, 'white', 'UAZ Patriot', True),
    ]
    print('\n\tDemonstration of all cars')
    for car in car_fleet:
        print(car)

    print('\n\tStarting all cars')
    for car in car_fleet:
        car.go()
        car.show_speed()
        print(car)

    print('\n\tStopping all cars')
    for car in car_fleet:
        car.stop()
        car.show_speed()
        print(car)

    print('\n\tFinal demonstration of all cars')
    for car in car_fleet:
        print(car)


if __name__ == '__main__':
    print(__doc__)
    main()
