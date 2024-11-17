from console import ConsoleWindow, Location
from console.controls.checkbox import Checkbox


class MyWindow(ConsoleWindow):
    def __init__(self):
        super().__init__()
        self.control = Checkbox()
        self.control.location = Location(10, 50)
        self.add(self.control)
        self.times: int = 0


main = MyWindow()
main.show()
