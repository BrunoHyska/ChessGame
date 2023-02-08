class Position:
    x = str
    y = str

    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.pos = self.y + self.x

    def __str__(self):
        return self.x + self.y