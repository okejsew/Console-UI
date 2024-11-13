import curses
from typing import Optional

from console.control import Control
from console.controls.label import Label
from console.event import MouseClickEventArgs
from console.layout import Location


class ConsoleWindow:
    def __init__(self):
        self.window: Optional[curses.window] = None
        self.controls: list[Control] = []

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
        curses.wrapper(self._show)

    def _show(self, window: curses.window):
        self.setup(window)
        while True:
            self.update()
            key = self.window.getch()
            if self.key_handler(key):
                break

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

    def check_mouse_click(self, y: int, x: int, button: int):
        for control in self.controls:
            if (y, x) in control.get_plist():
                control.on_click(MouseClickEventArgs(y, x, button))

    def key_handler(self, key: int) -> bool:
        if key == ord('q'):
            self.end()
            return True
        elif key == curses.KEY_MOUSE:
            _, x, y, button, _ = curses.getmouse()
            self.check_mouse_click(y, x, button)
        return False

    def next(self, cwin: 'ConsoleWindow'):
        self.end()
        cwin.show()

    def end(self):
        self.window.clear()
        curses.endwin()
