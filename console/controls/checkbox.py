from console.control import Control
from console.layout import Location
from console.events.key_pressed import KeyPressedEventArgs


class Checkbox(Control):
    def __init__(self, location: Location = Location(), text: str = 'Checkbox', style: str = '[{}] {}', fill: str = '*'):
        super().__init__(location)
        self.text = text
        self.style = style
        self.fill = fill

        self.checked: bool = False
        self.setup_events()

    def setup_events(self):
        self.event.mouse_click.set(self.on_click)
        self.event.key_pressed.set(self.key_pressed)

    def key_pressed(self, e: KeyPressedEventArgs):
        if e.key == ord('\n'):
            self.on_click(None)

    def on_click(self, _):
        self.checked = not self.checked

    def __str__(self):
        return self.style.format(self.fill if self.checked else ' ', self.text)
