from typing import Callable, Optional


class Event:
    def __init__(self):
        self.output: Optional[Callable] = None

    def __call__(self, *args, **kwargs):
        if self.output:
            self.output(*args, **kwargs)

    def __iadd__(self, output: Callable):
        self.output = output
        return self

class MouseClickEventArgs:
    def __init__(self, y: int, x: int, button: int):
        self.x: int = x
        self.y: int = y
        self.button: int = button