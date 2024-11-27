from dataclasses import dataclass

from multipledispatch import dispatch

from console.control import Control
from console.layout import Location


@dataclass
class Point:
    sign: str
    position: Location


class Canvas(Control):
    def __init__(self, location: Location, width: int = 15, height: int = 5, border: bool = True):
        super().__init__(location)
        self.width = width
        self.height = height
        self.points: list[Point] = []
        self.border: bool = border

    @dispatch(Location, str)
    def set_point(self, location: Location, sign: str):
        self.points.append(Point(sign.replace('\n', ' '), location))

    @dispatch(int, int, str)
    def set_point(self, y: int, x: int, sign: str):
        self.points.append(Point(sign.replace('\n', ' '), Location(y, x)))

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
