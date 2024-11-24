from console.events.key_pressed import KeyPressedEvent
from console.events.mouse_click import MouseClickEvent
from console.events.mouse_enter import MouseEnterEvent
from console.events.mouse_exit import MouseExitEvent


class EventManager:
    def __init__(self):
        self.mouse_click: MouseClickEvent = MouseClickEvent()
        self.key_pressed: KeyPressedEvent = KeyPressedEvent()
        self.mouse_enter: MouseEnterEvent = MouseEnterEvent()
        self.mouse_exit: MouseExitEvent = MouseExitEvent()
