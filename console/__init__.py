import curses
from typing import Optional

from console.control import Control
from console.controls.label import Label
from console.layout import Location


class ConsoleWindow:
    def __init__(self):
        self.is_showing: bool = False
        self.window: Optional[curses.window] = None
        self.controls: list[Control] = []
        self.focus: Optional[Control] = None

    def add(self, control: Control):
        if control not in self.controls:
            self.controls.append(control)
            control.parent = self

    def setup(self, window):
        self.window = window
        curses.raw()
        curses.curs_set(0)
        curses.noecho()
        curses.mousemask(curses.ALL_MOUSE_EVENTS)

    def show(self):
        self.is_showing = True
        curses.wrapper(self._show)

    def _show(self, window: curses.window):
        self.setup(window)
        while self.is_showing:
            self.update()
            key = self.window.getch()
            self.key_handler(key)

    def update(self):
        self.window.clear()
        for control in self.controls:
            if not control.visible: continue
            lines = str(control).split('\n')
            for i, line in enumerate(lines):
                self.draw_line(line, control.location.y + i, control.location.x)
        self.window.refresh()

    def draw_line(self, line: str, y: int, x: int):
        for i, char in enumerate(line):
            self.draw_char(char, y, x + i)

    def draw_char(self, char: str, y: int, x: int):
        try:
            self.window.addch(y, x, char)
        except Exception as ex:
            str(ex)

    def check_mouse_click(self, y: int, x: int):
        void_clicked = True
        for control in self.controls:
            if (y, x) in control.get_plist():
                control.event.on_click()
                self.focus = control
                void_clicked = False
        if void_clicked:
            self.focus = None

    def key_handler(self, key: int):
        if key == ord('q'):
            self.end()
        elif key == curses.KEY_MOUSE:
            _, x, y, button, _ = curses.getmouse()
            self.check_mouse_click(y, x)
        else:
            if self.focus:
                self.focus.event.on_key(key)


    def next(self, cwin: 'ConsoleWindow'):
        self.end()
        cwin.show()

    def end(self):
        self.is_showing = False
        self.window.clear()
        curses.endwin()
