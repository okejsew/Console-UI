from typing import Callable, Optional

from console.event import Event

class OnKeyPressedEventArgs:
    def __init__(self, key: int):
        self.key = key

class OnKeyPressedEvent(Event):
    def __init__(self):
        super().__init__()
        self.output: Optional[Callable[[OnKeyPressedEventArgs], None]] = None

    def set_output(self, output: Callable[[OnKeyPressedEventArgs], None]):
        super().set_output(output)
