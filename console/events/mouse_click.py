from typing import Callable, Optional

from console.event import Event

class MouseClickEventArgs:
    def __init__(self, y: int, x: int, btn_id: int):
        self.y, self.x, self.btn_id = y, x, btn_id

class MouseClickEvent(Event):
    def __init__(self):
        super().__init__()
        self.output: Optional[Callable[[MouseClickEventArgs], None]] = None

    def set(self, output: Callable[[MouseClickEventArgs], None]):
        super().set(output)