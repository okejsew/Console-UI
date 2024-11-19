from console.events.mouse_click import MouseClickEvent
from console.events.on_key import OnKeyPressedEvent


class EventManager:
    def __init__(self):
        self.on_click: MouseClickEvent = MouseClickEvent()
        self.on_key: OnKeyPressedEvent = OnKeyPressedEvent()