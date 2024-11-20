from console.events.mouse_click import MouseClickEvent
from console.events.key_pressed import KeyPressedEvent


class EventManager:
    def __init__(self):
        self.on_click: MouseClickEvent = MouseClickEvent()
        self.on_key: KeyPressedEvent = KeyPressedEvent()