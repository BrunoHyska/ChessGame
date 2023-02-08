from position import Position


class ChessFigure:
    letter = str
    color = str
    title = str
    position = Position

    def __init__(self, color, position):
        self.color = color
        self.position = position

    def __str__(self):
        if self.color == "black":
            return self.letter
        else:
            return '\033[94m' + self.letter + '\033[0m'

    def move(self, start, end):
        pass



