import curses

from console.controls.progressbar import ProgressBar
from console.events.key_pressed import KeyPressedEventArgs
from console.events.mouse_click import MouseClickEventArgs


class Slider(ProgressBar):
    def __init__(self):
        super().__init__()
        self.event.mouse_click.set(self.mouse_click)
        self.event.key_pressed.set(self.key_pressed)
        self.fill = '-'
        self.slider = '+'

    def mouse_click(self, e: MouseClickEventArgs):
        self.value = e.x - self.location.x

    def key_pressed(self, e: KeyPressedEventArgs):
        match e.key:
            case curses.KEY_LEFT:
                self.value -= 1
            case curses.KEY_RIGHT:
                self.value += 1
        self.check()

    def __str__(self):
        self.check()
        line = self.get_filling() + self.slider
        result = self.style.format(line.ljust(self.width))
        if self.show_percents:
            result += f' {self.get_percents()}%'
        return result
