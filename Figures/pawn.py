from chess_figure import ChessFigure


class Pawn(ChessFigure):
    letter = "P"
    title = "Pawn"
    first_move = True

    def move(self, start, end):
        if self.first_move:
            if start.y.lower() == end.y.lower() and abs(int(start.x) - int(end.x)) <= 2:
                self.first_move = False
                return True
            else:
                print("Invalid Move!")
        else:
            if start.y.lower() == end.y.lower() and abs(int(start.x) - int(end.x)) == 1:
                return True
            else:
                print("Invalid Move!")
        return False

    def beat(self, start, end, beaten):
        if abs(ord(start.y.upper()) - ord(end.y.upper())) == 1 and (int(start.x) - int(end.x) == 1 or int(end.x) - int(start.x) == 1):
            if beaten.title == "King":
                print("CheckMate!!! " + beaten.color + "'s king is under attack")
                return False
            return True
        print("Invalid Move! Pawns can only beat diagonally")
        return False
