import curses

from console.control import Control
from console.layout import Location
from console.events.key_pressed import KeyPressedEventArgs
from console.events.mouse_click import MouseClickEventArgs


class DropDown(Control):
    def __init__(self,
                 location: Location = Location(),
                 width: int = 10,
                 max_drop: int = 5,
                 style: str = '[ {} ]',
                 list_style: str = '| {} |',
                 sign: dict[bool, str] = None,
                 items: list[str] = None,
                 index: int = 0,
                 sindex: int = 0):
        super().__init__(location)
        sign = {False: '>', True: 'v'} if sign is None else sign
        items = [] if items is None else items
        self.items, self.sign = items, sign
        self.index, self.sindex = index, sindex
        self.width, self.max_drop = width, max_drop
        self.style, self.list_style = style, list_style

        self.__is_open: bool = False
        self.setup_events()

    def setup_events(self):
        self.event.mouse_click.set(self.mouse_click)
        self.event.key_pressed.set(self.key_pressed)

    def switch(self):
        self.__is_open = not self.__is_open

    def change_item(self, value: int):
        if not self.__is_open:
            self.index += value
            self.sindex = self.index
        else:
            self.sindex += value
        self.check()

    def key_pressed(self, e: KeyPressedEventArgs):
        if e.key == curses.KEY_UP:
            self.change_item(-1)
        elif e.key == curses.KEY_DOWN:
            self.change_item(1)

    def mouse_click(self, e: MouseClickEventArgs):
        x, y = e.x - self.location.x, e.y - self.location.y
        if x == 0 and y == 0:
            self.switch()
        else:
            if y > 0 and x > 2:
                self.index = y + self.sindex - 1
                self.sindex = self.index
                self.__is_open = False

    def check(self):
        self.index = min(len(self.items) - 1, max(self.index, 0))
        self.sindex = min(len(self.items) - self.max_drop, max(self.sindex, 0))

    def normalize(self, string: str) -> str:
        return (f'{string[:self.width - 2]}..' if len(string) >= self.width else string).ljust(self.width)

    def __str__(self):
        # Сырой стиль dropdown готовый к форматированию
        sign = self.sign[self.__is_open]
        dropdown_raw = '{} {}\n'.format(sign, self.style)

        if not len(self.items):  # Если нет элементов, возвращаем пустой dropdown
            return dropdown_raw.format(self.normalize(''))

        self.check()  # Стабилизируем индексы во избежание ошибок и добавляем текст
        dropdown = dropdown_raw.format(self.normalize(self.items[self.index]))
        if not self.__is_open:  # Возвращаем если dropdown закрыт
            return dropdown

        # Вычисляем какие элементы нужно показать в выпавшем списке
        up_limit = min(self.sindex + self.max_drop, len(self.items))
        for item in self.items[self.sindex:up_limit]:  # Готовим и добавляем к dropdown'у
            dropdown += f'  {self.list_style.format(self.normalize(item))}\n'
        return dropdown
