import curses
import time
from threading import Thread
from typing import Optional

from console.control import Control
from console.controls.label import Label
from console.events.mouse_click import MouseClickEventArgs
from console.events.key_pressed import KeyPressedEventArgs
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
        self.window.nodelay(True)
        curses.curs_set(0)
        curses.noecho()
        curses.mousemask(curses.ALL_MOUSE_EVENTS)

    def show(self):
        self.is_showing = True
        curses.wrapper(self._show)

    def rendering(self):
        while self.is_showing:
            self.window.clear()
            self.render_controls()
            self.render_mouse()
            self.window.refresh()
            time.sleep(0.016)

    def _show(self, window: curses.window):
        self.setup(window)
        Thread(target=self.rendering).start()
        while self.is_showing:
            key = self.window.getch()
            self.key_handler(key)

    def render_controls(self):
        for control in self.controls:
            if not control.visible: continue
            lines = str(control).split('\n')
            for oy, line in enumerate(lines):
                for ox, char in enumerate(line):
                    self.addch(char, control.location.y + oy, control.location.x + ox)

    def render_mouse(self):
        y, x, _ = self.get_mouse()
        if x != 0 and y != 0:
            self.addch('*', y, x)

    @staticmethod
    def get_mouse() -> tuple[int, int, int]:
        _, x, y, _, button = curses.getmouse()
        return y, x, button

    def addch(self, char: str, y: int, x: int):
        max_y, max_x = self.window.getmaxyx()
        if 0 < y < max_y and 0 < x < max_x:
            self.window.addch(y, x, char)

    def click_handler(self):
        void_clicked: bool = True
        y, x, btn = self.get_mouse()
        for control in self.controls:
            start_y, start_x = control.location.y, control.location.x
            size_y, size_x = control.get_size()
            if start_y <= y < start_y + size_y and start_x <= x < start_x + size_x:
                control.event.on_click(MouseClickEventArgs(y, x, btn))
                self.focus = control
                void_clicked = False
        if void_clicked:
            self.focus = None

    def key_handler(self, key: int):
        if key == -1:
            return

        if key == ord('q'):
            self.end()
        elif key == curses.KEY_MOUSE:
            self.click_handler()
        elif self.focus:
            self.focus.event.on_key(KeyPressedEventArgs(key))

    def next(self, cwin: 'ConsoleWindow'):
        self.end()
        cwin.show()

    def end(self):
        self.is_showing = False
        self.window.clear()
        curses.endwin()
