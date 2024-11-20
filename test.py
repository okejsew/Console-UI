from random import randint

from console import ConsoleWindow, Location
from console.controls.button import Button
from console.controls.checkbox import Checkbox
from console.controls.label import Label
from console.controls.progressbar import ProgressBar
from console.controls.textbox import TextBox


class MyWindow(ConsoleWindow):
    def __init__(self):
        super().__init__()
        self.textbox = TextBox()
        self.textbox.location = Location(1, 1)

        self.button = Button()
        self.button.location = Location(5, 1)
        self.button.event.on_click.set(self.shimmy)

        self.label = Label()
        self.label.location = Location(7, 1)

        self.pb = ProgressBar()
        self.pb.location = Location(9, 1)
        self.pb.value = 7
        self.pb.width = 25
        self.pb.show_percents = True

        self.cb = Checkbox()
        self.cb.location = Location(11, 1)

        self.add(self.textbox)
        self.add(self.label)
        self.add(self.button)
        self.add(self.cb)
        self.add(self.pb)
        self.times: int = 0

    def shimmy(self, e): # noqa
        self.button.location = Location(randint(2, 25), randint(2, 117))
        self.label.text = f'Button Location: {self.button.location}'
        self.pb.value = randint(0, 11)

main = MyWindow()
main.show()
