from typing import Callable

from console.event import Event

class MouseEnterEventArgs:
    def __init__(self, x, y):
        self.x, self.y = x, y

class MouseEnterEvent(Event):
    def __init__(self):
        super().__init__()

    def set(self, output: Callable[[MouseEnterEventArgs], None]):
        super().set(output)