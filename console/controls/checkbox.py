from console import Control


class Checkbox(Control):
    def __init__(self):
        super().__init__()
        self.text: str = 'Checkbox'
        self.checked: bool = False
        self.event.on_click.set(self.on_click)

    def on_click(self, e):  # noqa
        self.checked = not self.checked

    def __str__(self):
        return f'[{"*" if self.checked else " "}] {self.text}'
