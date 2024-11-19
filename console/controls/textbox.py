from console.control import TextControl
from console.events.on_key import OnKeyPressedEventArgs


class TextBox(TextControl):
    def __init__(self):
        super().__init__()
        self.readonly: bool = False
        self.event.on_key.set_output(self.__on_key)

    def __on_key(self, e: OnKeyPressedEventArgs):
        if not self.readonly:
            if e.key == 8:
                self.text = self.text[:-1]
            elif e.key == 13:
                self.text += '\n'
            else:
                self.text += chr(e.key)

    def __str__(self):
        sign = '*' if self.parent.focus is self else '┌'
        top = sign + '─' * len(self.text) + '┐\n'
        down = '└' + '─' * len(self.text) + '┘'
        text = f'│{self.text}│\n'
        return top + text + down
