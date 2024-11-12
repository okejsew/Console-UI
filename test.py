from console import ConsoleWindow, MouseClickEventArgs, Location
from console.controls.label import Label


class MyWindow(ConsoleWindow):
    def __init__(self):
        super().__init__()
        self.lbl_debug = Label()
        self.lbl_debug.on_click += self.lbl_debug_on_click
        self.lbl_debug.location = Location(10, 50)
        self.add(self.lbl_debug)
        self.times: int = 0

    def lbl_debug_on_click(self, e: MouseClickEventArgs):
        self.times += 1
        self.lbl_debug.set_text(f'Clicked {self.times} times'
                                f'\nMouse pos: {e.y}, {e.x}')


main = MyWindow()
main.show()
