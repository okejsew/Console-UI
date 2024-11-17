from console import Control

class ProgressBar(Control):
    def __init__(self):
        super().__init__()
        self.value: int = 0
        self.max_value: int = 10
        self.width: int = 10
        self.show_percents: bool = False

    def __str__(self):
        length = int(self.width * (self.value / self.max_value))
        result = '[{}]'.format(('#'*length).ljust(self.width))
        if self.show_percents:
            result += f' {int(self.value / self.max_value * 100)}%'
        return result
