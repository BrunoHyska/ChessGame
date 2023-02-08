from chess_figure import ChessFigure


class Bishop(ChessFigure):
    letter = "B"
    title = "Bishop"

    def move(self, start, end):
        if abs(int(start.x) - int(end.x)) == abs(ord(start.y) - ord(end.y)):
            return end
        else:
            print("Invalid Move!")
        return False

    def beat(self, start, end, beaten):
        if self.move(start, end):
            if beaten.title == "King":
                print("CheckMate!!! " + beaten.color + "'s king is under attack")
                return False
            return True
        return False
