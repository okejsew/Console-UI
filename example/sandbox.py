from random import shuffle

from console import *
from console.controls.canvas import Canvas

window = ConsoleWindow()
def mouse_click(_: MouseClickEventArgs):
    shuffle(l := list(btn.text))
    btn.text = ''.join(l)
    window.end()


controls = [
    btn := Button(Location(1, 1), 'Click ME'),
    Label(Location(3, 1), 'Just a regular label'),
    ProgressBar(Location(5, 1), 4, width=25),
    Slider(Location(7, 1), show_percents=True),
    TextBox(Location(13, 1), title='Почему бы и нет', placeholder='</>'),
    DropDown(Location(1, 30), items=[
        'Капучино', 'Мокачино', 'Айс Латте', 'Американо',
        'Эспрессо', 'Молочный Шоколад', 'Водичка']),
    Checkbox(Location(11, 1)),
    cnv := Canvas(Location(1, 50))
]
btn.event.mouse_click.set(mouse_click)
cnv.set_point(Location(3, 4), '@')

def start_example():
    window.controls = controls
    window.show()
