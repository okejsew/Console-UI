from console import Control, Location
from console.events.key_pressed import KeyPressedEventArgs


class TextBox(Control):
    def __init__(self,
                 location: Location = Location(),
                 text: str = '',
                 title: str = 'TextBox',
                 placeholder: str = 'Enter your text here',
                 readonly: bool = False,
                 border: dict[str, str] = None):
        super().__init__(location)
        border = {'tl': '┌', 'tr': '┐', 'bl': '└', 'br': '┘', 'wall': '│', 'ceil': '─'} if border is None else border
        self.text, self.title, self.border = text, title, border
        self.placeholder, self.readonly = placeholder, readonly
        self.setup_events()

    def setup_events(self):
        self.event.key_pressed.set(self.key_pressed)

    def key_pressed(self, e: KeyPressedEventArgs):
        if self.readonly:
            return
        if e.key == 8:
            self.text = self.text[:-1] if self.text else self.text
        elif e.key == 10:
            self.text += '\n'
        else:
            self.text += chr(e.key)

    def get_text_width(self, text: list[str]) -> int:
        return max(*[len(line) for line in text], len(self.title))

    def generate_title(self, width: int) -> str:
        return self.title.ljust(width, self.border['ceil'])

    def generate_ceiling(self, title: str) -> str:
        return self.border['tl'] + title + self.border['tr'] + '\n'

    def generate_floor(self, width) -> str:
        return self.border['bl'] + self.border['ceil'] * width + self.border['br']

    def frame(self, text: list[str]) -> str:
        textbox = ''
        width = self.get_text_width(text)
        title = self.generate_title(width)
        ceiling = self.generate_ceiling(title)
        floor = self.generate_floor(width)
        for line in text:
            textbox += self.border['wall'] + line.ljust(width) + self.border['wall'] + '\n'
        return ceiling + textbox + floor

    def __str__(self):
        if not self.text:
            return self.frame([self.placeholder])
        else:
            return self.frame(self.text.split('\n'))
