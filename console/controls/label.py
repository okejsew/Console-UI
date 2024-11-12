from console import Control


class Label(Control):
    def __init__(self):
        super().__init__()
        self.text: str = 'Label'

    def set_text(self, text: str):
        self.text = text
        self.parent.update()

    def __str__(self):
        return self.text
