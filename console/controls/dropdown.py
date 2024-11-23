import curses
from operator import index

from console import Control
from console.events.key_pressed import KeyPressedEventArgs
from console.events.mouse_click import MouseClickEventArgs


class DropDown(Control):
    def __init__(self):
        super().__init__()
        self.items: list[str] = [f'Item{i}' for i in range(100)] + ['rgheuihgie']
        self.index: int = 0
        self.sindex = 0
        self.sign_close = 'v'
        self.sign_open = '>'
        self.width = 10
        self.max_drop = 5

        self.__is_open: bool = False
        self.event.mouse_click.set(self.mouse_click)
        self.event.key_pressed.set(self.key_pressed)

    def switch(self):
        self.__is_open = not self.__is_open

    def key_pressed(self, e: KeyPressedEventArgs):
        if e.key == curses.KEY_UP:
            if not self.__is_open:
                self.index -= 1
                self.sindex = self.index
            else:
                self.sindex -= 1
        elif e.key == curses.KEY_DOWN:
            if not self.__is_open:
                self.index += 1
                self.sindex = self.index
            else:
                self.sindex += 1
        self.index = min(len(self.items)-1, max(self.index, 0))
        self.sindex = min(len(self.items)-self.max_drop, max(self.sindex, 0))

    def mouse_click(self, e: MouseClickEventArgs):
        x, y = e.x - self.location.x, e.y - self.location.y
        if x == 0 and y == 0:
            self.switch()
        else:
            if y > 0 and x > 2:
                self.index = y + self.sindex - 1
                self.sindex = self.index
                self.switch()

    def __str__(self):
        up_limit = self.sindex + self.max_drop if self.sindex + self.max_drop < len(self.items) else len(self.items)
        items = self.items[self.sindex:up_limit]

        text = self.items[self.index] if self.index < len(self.items) else ''
        text = f'{text[:self.width - 2]}..' if len(text) >= self.width else text
        text = text.ljust(self.width)

        dropdown = f'{self.sign_close if self.__is_open else self.sign_open} [ {text} ]\n'
        if self.__is_open:
            for item in items:
                item = f'{item[:self.width - 2]}..' if len(item) >= self.width else item
                dropdown += f'  | {item.ljust(self.width)} |\n'

        return dropdown
