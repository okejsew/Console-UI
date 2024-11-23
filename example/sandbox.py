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

window = ConsoleWindow()

def mouse_click(_: MouseClickEventArgs):
    l = list(btn.text)
    shuffle(l)
    btn.text = ''.join(l)

btn = Button()
btn.location = Location(1, 1)
btn.text = 'Click ME'
btn.event.mouse_click.set(mouse_click)

lbl = Label()
lbl.location = Location(3, 1)
lbl.text = 'Just a regular label'

pb = ProgressBar()
pb.location = Location(5, 1)
pb.value = 4
pb.width = 25

sld = Slider()
sld.location = Location(7, 1)
sld.show_percents = True

tb = TextBox()
tb.location = Location(13, 1)
tb.title = 'Почему бы и нет'
tb.placeholder = '</>'

dd = DropDown()
dd.location = Location(1, 30)
dd.items = ['Капучино', 'Мокачино', 'Айс Латте', 'Американо', 'Эспрессо', 'Молочный Шоколад', 'Водичка']

cb = Checkbox()
cb.location = Location(11, 1)


window.add(btn)
window.add(lbl)
window.add(cb)
window.add(pb)
window.add(tb)
window.add(dd)
window.add(sld)

def start_example():
    window.show()