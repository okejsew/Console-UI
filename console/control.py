from typing import Optional, TYPE_CHECKING

from console.event import Event
from console.layout import Location

if TYPE_CHECKING:
    from console import ConsoleWindow

class Control:
    def __init__(self):
        self.parent: Optional['ConsoleWindow' | ContainerControl] = None
        self.location: Location = Location()
        self.visible: bool = True

        self.on_click: Optional[Event] = Event()

    def get_plist(self) -> list[tuple]:
        positions = []
        lines = str(self).split('\n')
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                positions.append((self.location.y + y, self.location.x + x))
        return positions

    def __str__(self):
        return 'Control'


class InteractiveControl(Control):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'InveractiveControl'

class ContainerControl(Control):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'ContainerControl'
