from chess_figure import ChessFigure

class Rook(ChessFigure):
    letter = "R"
    title = "Rook"

    def move(self, start, end):
        if start.x == end.x or start.y == end.y:
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
