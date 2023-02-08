from chess_figure import ChessFigure

class King(ChessFigure):
    letter = "K"
    title = "King"

    def move(self, start, end):
        if abs(int(start.x) - int(end.x)) <= 1 and abs(ord(start.y) - ord(end.y)) <= 1:
            return end
        else:
            print("Invalid Move! King can only move one step in any direction.")
        return False

    def beat(self, start, end, beaten):
        if self.color == beaten.color:
            print("Invalid Move! You cannot beat your own pieces.")
            return False
        if self.move(start, end):
            return True
        return False



    def castling(self, start, end, rook):
        if (abs(start.x - end.x) <= 1) and (abs(start.y - end.y) <= 1):
            return False  # Not a valid castling, King moved too close
        if abs(start.x - end.x) != 2:
            return False  # Not a valid castling, King moved too far
        if start.x != rook.position.x:
            return False  # Rook is not on the same rank as King
        if abs(start.y - rook.position.y) != 3:
            return False  # Rook is not on the correct file

        path = [(start.x, i) for i in range(min(start.y, end[1]), max(start.y, end.y) + 1)]
        for i, pos in enumerate(path):
            if i == len(path) // 2:
                continue
            if pos == rook.position:
                continue
        # Valid castling
        return True
