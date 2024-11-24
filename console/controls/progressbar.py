from console import Control, Location


class ProgressBar(Control):
    def __init__(self,
                 location: Location = Location(),
                 value: int = 0,
                 max_value: int = 10,
                 width: int = 10,
                 show_percents: bool = False,
                 fill: str = '#',
                 style: str = '[{}]'):
        super().__init__(location)
        self.value, self.max_value = value, max_value
        self.width, self.show_percents = width, show_percents
        self.fill, self.style = fill, style

    def check(self):
        self.value = max(min(self.value, self.max_value), 0)

    def get_ratio(self):
        return self.value / self.max_value

    def get_percents(self):
        return round(self.get_ratio() * 100, 2)

    def get_filling(self):
        return self.fill * int(self.width * self.get_ratio())

    def __str__(self):
        self.check()
        result = self.style.format(self.get_filling().ljust(self.width))
        if self.show_percents:
            result += f' {self.get_percents()}%'
        return result
