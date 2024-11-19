from typing import Optional, TYPE_CHECKING

from console.event_manager import EventManager
from console.layout import Location

if TYPE_CHECKING:
    from console import ConsoleWindow

class Control:
    def __init__(self):
        self.parent: Optional['ConsoleWindow'] = None
        self.location: Location = Location()
        self.visible: bool = True
        self.event: EventManager = EventManager()

    def get_plist(self) -> list[tuple]:
        positions = []
        lines = str(self).split('\n')
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                positions.append((self.location.y + y, self.location.x + x))
        return positions

    def __str__(self):
        return 'Control'

class TextControl(Control):
    def __init__(self):
        super().__init__()
        self.text: str = 'TextControl'

    def set_text(self, new: str):
        self.text = new
        self.parent.update()