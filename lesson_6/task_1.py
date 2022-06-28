#!/usr/bin/env python3
""">>>\nThis module demonstrate Traffic Light with timing for it lights.
The instance of TrafficLight can be run continiously
while User didn't stop it.

Classes:
    TrafficLight

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
# TODO: оформить проверку аргумента через геттер и сеттер
import os
import threading as thr
from numpy.typing import NDArray as Array
from numpy import array as arr

from itertools import cycle
from time import sleep
from typing import TypeVar

Thread = TypeVar('Thread')


class TrafficLight:
    """This is a class for a simple three-color traffic light that can switch
    its lights alternately by drawing them in the console.

    Raises:
        ValueError: raises if the order of colors provided is invalid.
    """
    __color: tuple[str, str, str] = ('red', 'yellow', 'green')

    def __init__(self, traffic_colors: list[str], green_time: int) -> None:
        """Creates a Trafficlight object with the specified external
        parameters like colors of lights and delay time for green light.

        Arguments:
            traffic_colors -- ordered list of TrafficLight colors;
            green_time -- delay for green light of TrafficLight.
        """
        array_orders_compare: Array = (
            arr(traffic_colors) == arr(TrafficLight.__color)
        )
        is_order_correct: bool = all(array_orders_compare)
        if not is_order_correct:
            raise ValueError('Invalid order of colors provided!')
        self.color: list[str] = traffic_colors
        self.timing: dict[str, int] = {
            'red': 7,
            'yellow': 2,
            'green': green_time
        }

    def show_colored_light(self, color: str) -> None:
        """Shows in console coloring text.

        Arguments:
            color -- color of TrafficLight

        Returns:
            same string colored with the corresponding color
        """
        red = '\033[41m'
        yellow = '\033[43m'
        green = '\033[42m'
        light = '@'
        base = '\033[47m '
        clear = '\033[0m'
        if color is 'red':
            print(f' {red}{light:^3}{base*7}{clear}', end='\r')
        elif color is 'yellow':
            print(f' {base*3}{yellow}{light:^3}{base*4}{clear}', end='\r')
        elif color is 'green':
            print(f' {base*6}{green}{light:^3}{base}{clear}', end='\r')

    def running(self) -> None:
        """Running continiously TrafficLight object."""
        def _get_interrupt() -> None:
            """Thread function that catches interrupt for Trafficlight."""
            input('Press Enter to interrupt and exit.\n')
            os._exit(0)

        new_thread: Thread = thr.Thread(
            target=_get_interrupt,
            daemon=True
        )
        new_thread.start()
        for light in cycle(self.color):
            self.show_colored_light(light)
            sleep(self.timing[light])


def main() -> None:
    """The execution point for the program file."""
    colors: list[str] = ['red', 'yellow', 'green']
    #wrong_colors: list[str] = ['red', 'green', 'yellow']
    green_light_time: int = 2
    new_traffic = TrafficLight(colors, green_light_time)
    new_traffic.running()


if __name__ == '__main__':
    print(__doc__)
    main()
