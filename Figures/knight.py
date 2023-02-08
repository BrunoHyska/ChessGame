from chess_figure import ChessFigure


class Knight(ChessFigure):
    letter = "G"
    title = "Knight"

    def move(self, start, end):
        if abs(int(start.x) - int(end.x)) == 2 and abs(ord(start.y) - ord(end.y)) == 1 or abs(
                int(start.x) - int(end.x)) == 1 and \
                abs(ord(start.y) - ord(end.y)) == 2:
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