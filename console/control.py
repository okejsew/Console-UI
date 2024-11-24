from console.eventman import EventManager
from console.layout import Location


class Control:
    def __init__(self, location: Location = Location()):
        self.visible: bool = True
        self.location: Location = location
        self.event: EventManager = EventManager()

    def get_size(self) -> tuple[int, int]:
        text = str(self).split('\n')
        size_y = len(text)
        size_x = max(len(line) for line in text)
        return size_y, size_x

    def __str__(self):
        return 'Control'
