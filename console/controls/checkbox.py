from console.control import TextControl


class Checkbox(TextControl):
    def __init__(self):
        super().__init__()
        self.text: str = 'Checkbox'
        self.checked: bool = False
        self.event.on_click += self.__check

    def __check(self):
        self.checked = not self.checked

    def __str__(self):
        return f'[{"*" if self.checked else " "}] {self.text}'
