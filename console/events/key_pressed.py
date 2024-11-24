from typing import Callable, Optional

from console.event import Event


class KeyPressedEventArgs:
    def __init__(self, key: int):
        self.key = key


class KeyPressedEvent(Event):
    def __init__(self):
        super().__init__()
        self.output: Optional[Callable[[KeyPressedEventArgs], None]] = None

    def set(self, output: Callable[[KeyPressedEventArgs], None]):
        super().set(output)
