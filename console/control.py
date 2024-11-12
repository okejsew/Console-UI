from typing import Optional, TYPE_CHECKING

from console.event import Event
from console.layout import Location

if TYPE_CHECKING:
    from console import ConsoleWindow

class Control:
    def __init__(self):
        self.parent: Optional['ConsoleWindow'] = None
        self.on_click: Optional[Event] = Event()
        self.location: Location = Location()
        self.visible: bool = True

    def __str__(self):
        return 'Control'


class InteractiveControl(Control):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'InveractiveControl'
