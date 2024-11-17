from console.control import TextControl

class Button(TextControl):
    def __init__(self):
        super().__init__()
        self.text: str = 'Button'

    def __str__(self):
        return f'[ {self.text} ]'