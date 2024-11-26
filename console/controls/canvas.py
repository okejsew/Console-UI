from dataclasses import dataclass
from multipledispatch import dispatch
from pymsgbox import boxRoot

from console.control import Control
from console.events.mouse_click import MouseClickEventArgs
from console.layout import Location

@dataclass
class Point:
    sign: str
    position: Location

class Canvas(Control):
    def __init__(self, location: Location):
        super().__init__(location)
        self.width = 15
        self.height = 5
        self.points: list[Point] = []
        self.border: bool = True
        self.setup_events()

    def setup_events(self):
        self.event.mouse_click.set(self.mouse_click)

    def mouse_click(self, e: MouseClickEventArgs):
        y, x = e.y - self.location.y, e.x - self.location.x
        if self.border:
            self.set_point(Location(y-1, x-1), '@')
        else:
            self.set_point(Location(y, x), '@')

    @dispatch(Location, str)
    def set_point(self, location: Location, sign: str):
        self.points.append(Point(sign, location))

    @dispatch(int, int, str)
    def set_point(self, y: int, x: int, sign: str):
        self.points.append(Point(sign, Location(y, x)))

    def __str__(self):
        buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for point in self.points:
            y, x = point.position.y, point.position.x
            if 0 <= x < len(buffer[0]) and 0 <= y < len(buffer):
                buffer[point.position.y][point.position.x] = point.sign
        if self.border:
            ceiling = '┌' + '─' * self.width + '┐\n'
            for line in buffer:
                ceiling += '│' + ''.join(line) + '│\n'
            ceiling += '└' + '─' * self.width + '┘'
            return ceiling
        else:
            text = ''
            for line in buffer:
                text += ''.join(line) + '\n'
            return text