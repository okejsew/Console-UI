from typing import Callable, Optional


class Event:
    def __init__(self):
        self.output: Optional[Callable] = None

    def __call__(self, *args, **kwargs):
        if self.output:
            self.output(*args, **kwargs)

    def set(self, output: Callable):
        self.output = output
