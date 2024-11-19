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

class EventManager:
    def __init__(self):
        self.on_click: Event = Event()
        self.on_key: Event = Event()