class Location:
    def __init__(self, y: int = 0, x: int = 0):
        self.y: int = y
        self.x: int = x

    def __str__(self):
        return f'Location({self.y}, {self.x})'
