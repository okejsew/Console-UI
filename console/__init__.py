import curses
import time
from threading import Thread
from typing import Optional

from console.control import Control
from console.events.key_pressed import KeyPressedEventArgs
from console.events.mouse_click import MouseClickEventArgs
from console.events.mouse_enter import MouseEnterEventArgs
from console.layout import Location


class ConsoleWindow:
    def __init__(self):
        self.is_showing: bool = False

        self.window: Optional[curses.window] = None
        self.focus: Optional[Control] = None
        self.thread: Optional[Thread] = None

        self.controls: list[Control] = []
        self.prev_controls: list[Control] = []
        self.curr_controls: list[Control] = []

    def add(self, control: Control):
        if control not in self.controls:
            self.controls.append(control)
            control.parent = self

    def setup(self, window):
        self.window = window
        self.window.nodelay(True)
        self.window.keypad(True)
        curses.curs_set(0)
        curses.noecho()
        curses.mousemask(curses.ALL_MOUSE_EVENTS)

    def show(self):
        self.is_showing = True
        curses.wrapper(self._show)

    def force_end(self, ex: Exception):
        self.end()
        input(f'Произошла ошибка: {ex}')

    def renderer(self):
        exception = None
        while self.is_showing:
            try:
                self.window.clear()
                self.render_controls()
                self.window.refresh()
                time.sleep(0.016)
            except Exception as ex:
                exception = ex
                break
        self.force_end(exception)


    def _show(self, window: curses.window):
        self.setup(window)
        self.thread = Thread(target=self.renderer)
        self.thread.start()
        exception = None
        while self.is_showing:
            try:
                self.update_mouse()
                key = self.window.getch()
                self.key_handler(key)
                self.mouse_handler()
            except Exception as ex:
                exception = ex
                break
        self.force_end(exception)

    def render_controls(self):
        for control in self.controls:
            if not control.visible: continue
            lines = str(control).split('\n')
            for oy, line in enumerate(lines):
                for ox, char in enumerate(line):
                    self.addch(char, control.location.y + oy, control.location.x + ox)

    def addch(self, char: str, y: int, x: int):
        max_y, max_x = self.window.getmaxyx()
        if 0 <= y < max_y and 0 <= x < max_x:
            self.window.addch(y, x, char)

    @staticmethod
    def get_mouse() -> tuple[int, int, int]:
        _, x, y, _, button = curses.getmouse()
        return y, x, button

    def update_mouse(self):
        y, x, _ = self.get_mouse()
        self.curr_controls.clear()
        for control in self.controls:
            start_y, start_x = control.location.y, control.location.x
            size_y, size_x = control.get_size()
            if start_y <= y < start_y + size_y and start_x <= x < start_x + size_x:
                self.curr_controls.append(control)

    def click_handler(self):
        void_clicked: bool = True
        y, x, btn = self.get_mouse()
        for control in self.curr_controls:
            control.event.mouse_click(MouseClickEventArgs(y, x, btn))
            self.focus = control
            void_clicked = False
        if void_clicked:
            self.focus = None

    def mouse_handler(self):
        y, x, _ = self.get_mouse()
        for control in self.curr_controls:
            if control not in self.prev_controls:
                control.event.mouse_enter(MouseEnterEventArgs(x, y))
        for control in self.prev_controls:
            if control not in self.curr_controls:
                control.event.mouse_exit()
        self.prev_controls = self.curr_controls.copy()
        self.curr_controls = []

    def key_handler(self, key: int):
        if key == -1:
            return
        if key == ord('q'):
            self.end()
        elif key == curses.KEY_MOUSE:
            self.click_handler()
        elif self.focus:
            self.focus.event.key_pressed(KeyPressedEventArgs(key))

    def next(self, cwin: 'ConsoleWindow'):
        self.end()
        cwin.show()

    def end(self):
        self.is_showing = False
        try:
            self.thread.join()
        except Exception as ex:
            print(f'Ошибка произошла не в главном потоке ({ex})')
        self.window.clear()
        curses.endwin()
