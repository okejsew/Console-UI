from console.controls.progressbar import ProgressBar
from console.events.mouse_click import MouseClickEventArgs


class Slider(ProgressBar):
    def __init__(self):
        super().__init__()
        self.event.mouse_click.set(self.mouse_click)

    def mouse_click(self, e: MouseClickEventArgs):
        self.value = e.x - self.location.x

    def __str__(self):
        self.value = max(min(self.value, self.max_value), 0)
        length = int(self.width * (self.value / self.max_value))
        line = '-'*(length-1) + '+'
        result = f'[{line.ljust(self.width)}]'
        if self.show_percents:
            result += f' {int(self.value / self.max_value * 100)}%'
        return result