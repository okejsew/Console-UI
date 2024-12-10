from console.controls.progressbar import ProgressBar
from console.events.key_pressed import KeyPressedEventArgs
from console.events.mouse_click import MouseClickEventArgs
from console.layout import Location


class Slider(ProgressBar):
    def __init__(self, location: Location = Location(), value: int = 0, max_value: int = 10, width: int = 10,
                 show_percents: bool = False, fill: str = '-', style: str = '[{}]', slider: str = '+'):
        super().__init__(location, value, max_value, width, show_percents, fill, style)
        self.event.mouse_click.set(self.mouse_click)
        self.event.key_pressed.set(self.key_pressed)
        self.slider = slider

    def mouse_click(self, e: MouseClickEventArgs):
        self.value = e.x - self.location.x

    def key_pressed(self, e: KeyPressedEventArgs):
        match e.key:
            case 260:
                self.value -= 1
            case 261:
                self.value += 1
        self.check()

    def __str__(self):
        self.check()
        line = self.get_filling()[:-1] + self.slider
        result = self.style.format(line.ljust(self.width))
        if self.show_percents:
            result += f' {self.get_percents()}%'
        return result
