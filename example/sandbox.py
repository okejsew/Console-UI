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
    l = list(btn.text)
    shuffle(l)
    btn.text = ''.join(l)

btn = Button(Location(1, 1), 'Click ME')
btn.event.mouse_click.set(mouse_click)

lbl = Label(Location(3, 1), 'Just a regular label')

pb = ProgressBar(Location(5, 1), 4, width=25)

sld = Slider(Location(7, 1), show_percents=True)

tb = TextBox(Location(13, 1), title='Почему бы и нет', placeholder='</>')

items = ['Капучино', 'Мокачино', 'Айс Латте', 'Американо', 'Эспрессо', 'Молочный Шоколад', 'Водичка']
dd = DropDown(Location(1, 30), items=items)

cb = Checkbox(Location(11, 1))

window = ConsoleWindow([btn, lbl, pb, sld, tb, dd, cb])

def start_example():
    window.show()