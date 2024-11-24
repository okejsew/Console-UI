class Location:
    def __init__(self, y: int = 0, x: int = 0):
        """
        Структура для позиционирования элементов на экране
        :param y: Позиция по y-оси (чем больше, тем ниже элемент)
        :param x: Позиция по x-оси (чем больше, тем правее элемент)
        """
        self.y: int = y
        self.x: int = x

    def __str__(self):
        return f'Location({self.y}, {self.x})'
