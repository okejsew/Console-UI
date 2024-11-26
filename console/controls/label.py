from console.control import Control
from console.layout import Location


class Label(Control):
    def __init__(self, location: Location = Location(), text: str = 'Label'):
        super().__init__(location)
        self.text = text

    def __str__(self):
        return self.text
