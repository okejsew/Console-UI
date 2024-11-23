import curses

from console import Control
from console.events.key_pressed import KeyPressedEventArgs


class Checkbox(Control):
    def __init__(self):
        super().__init__()
        self.text: str = 'Checkbox'
        self.checked: bool = False
        self.event.mouse_click.set(self.on_click)
        self.event.key_pressed.set(self.key_pressed)

    def key_pressed(self, e: KeyPressedEventArgs):
        if e.key == ord('\n'):
            self.on_click(None)

    def on_click(self, _):
        self.checked = not self.checked

    def __str__(self):
        return f'[{"*" if self.checked else " "}] {self.text}'
