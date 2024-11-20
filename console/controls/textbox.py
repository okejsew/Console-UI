from console import Control
from console.events.key_pressed import KeyPressedEventArgs
from console.keys import Keys


class TextBox(Control):
    def __init__(self):
        super().__init__()
        self.text = ''
        self.title = 'TextBox'
        self.placeholder = 'Enter your text here'
        self.readonly: bool = False
        self.event.key_pressed.set(self.key_pressed)

    def key_pressed(self, e: KeyPressedEventArgs):
        if e.key == Keys.BACKSPACE:
            self.text = self.text[:-1] if self.text else self.text
        elif e.key == 10:
            self.text += '\n'
        elif 32 <= e.key <= 126:
            self.text += chr(e.key)

    def __str__(self):
        text = self.text.split('\n') if self.text else [self.placeholder]
        size_x = max(*[len(line) for line in text], len(self.title))

        result = f'┌{self.title.ljust(size_x, "─")}┐\n'
        for line in text:
            result += f'│{line.ljust(size_x)}│\n'
        result += '└' + '─' * size_x + '┘'

        return result
