from console import ConsoleWindow, Location
from console.controls.textbox import TextBox


class MyWindow(ConsoleWindow):
    def __init__(self):
        super().__init__()
        self.control = TextBox()
        self.control.location = Location(10, 50)
        self.add(self.control)
        self.times: int = 0


main = MyWindow()
main.show()
