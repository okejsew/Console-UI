from console import Control


class ProgressBar(Control):
    def __init__(self):
        super().__init__()
        self.value: int = 0
        self.max_value: int = 10
        self.width: int = 10
        self.show_percents: bool = False

        self.fill = '#'
        self.style = '[{}]'

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
