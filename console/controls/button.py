from console.control import Control
from console.layout import Location


class Button(Control):
    def __init__(self, location: Location = Location(), text: str = 'Button', style: str = '[ {} ]', focused_style: str = ' [{}] '):
        super().__init__(location)
        self.text: str = text
        self.style = style
        self.focused_style = focused_style

        self.__focused = False
        self.setup_events()

    def setup_events(self):
        self.event.mouse_enter.set(self.mouse_enter)
        self.event.mouse_exit.set(self.mouse_exit)

    def mouse_enter(self, _):
        self.__focused = True

    def mouse_exit(self):
        self.__focused = False

    def __str__(self):
        if self.__focused:
            return self.focused_style.format(self.text)
        else:
            return self.style.format(self.text)