from console import Control

class Button(Control):
    def __init__(self):
        super().__init__()
        self.text: str = 'Button'
        self.buffer: str = ''
        self.event.mouse_enter.set(self.mouse_enter)
        self.event.mouse_exit.set(self.mouse_exit)

    def mouse_enter(self):
        self.buffer = self.text
        self.text = self.text.upper()

    def mouse_exit(self):
        self.text = self.buffer

    def __str__(self):
        return f'[ {self.text} ]'