from console import Control

class Button(Control):
    def __init__(self):
        super().__init__()
        self.text: str = 'Button'
        self.event.mouse_enter.set(self.mouse_enter)
        self.event.mouse_exit.set(self.mouse_exit)
        self.__focused = False

    def mouse_enter(self):
        self.__focused = True

    def mouse_exit(self):
        self.__focused = False

    def __str__(self):
        return f'[:{self.text}:]' if self.__focused else f'[ {self.text} ]'