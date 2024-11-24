from random import shuffle

from console import ConsoleWindow, Location
from console.controls.button import Button
from console.controls.checkbox import Checkbox
from console.controls.dropdown import DropDown
from console.controls.label import Label
from console.controls.progressbar import ProgressBar
from console.controls.slider import Slider
from console.controls.textbox import TextBox
from console.events.mouse_click import MouseClickEventArgs


def mouse_click(_: MouseClickEventArgs):
    shuffle(l := list(btn.text))
    btn.text = ''.join(l)


controls = [
    btn := Button(Location(1, 1), 'Click ME'),
    Label(Location(3, 1), 'Just a regular label'),
    ProgressBar(Location(5, 1), 4, width=25),
    Slider(Location(7, 1), show_percents=True),
    TextBox(Location(13, 1), title='Почему бы и нет', placeholder='</>'),
    DropDown(Location(1, 30), items=[
        'Капучино', 'Мокачино', 'Айс Латте', 'Американо',
        'Эспрессо', 'Молочный Шоколад', 'Водичка']),
    Checkbox(Location(11, 1))
]
btn.event.mouse_click.set(mouse_click)

def start_example():
    ConsoleWindow(controls).show()
