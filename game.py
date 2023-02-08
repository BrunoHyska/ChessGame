from Figures.king import King
from Figures.bishop import Bishop
from Figures.queen import Queen
from Figures.pawn import Pawn
from Figures.rook import Rook
from Figures.knight import Knight
from position import Position

turn = ""

class ChessBoard:
    def __init__(self):
        self.board = self.construct()

    def construct(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        colors = ['white', 'black']

        for row, color in zip([1, 6], colors):
            for col in range(8):
                position = columns[col] + str(2 if color == 'white' else 7)
                board[row][col] = Pawn(color, position)

        for row, color in zip([0, 7], colors):
            for col, piece in zip(range(8), pieces):
                position = columns[col] + str(row + 1)
                board[row][col] = piece(color, position)
        return board

    def display(self):
        for row in self.board:
            for i in row:
                if i:
                    print(i, end=" ")
                else:
                    print(".", end=" ")
            print(" ")



    def make_move(self, start_pos, end_pos):
        start_x, start_y = ord(start_pos[0].upper()) - ord('A'), int(start_pos[1]) - 1
        end_x, end_y = ord(end_pos[0].upper()) - ord('A'), int(end_pos[1]) - 1
        start = Position(start_pos[0], start_pos[1])
        end = Position(end_pos[0], end_pos[1])

        piece = self.board[start_y][start_x]
        if piece is None:
            print("No piece found at the starting position.")
        else:
            global turn
            if turn != piece.color:
                turn = piece.color

                if self.board[end_y][end_x] is None:
                    if piece.move(start, end):
                        self.board[end_y][end_x] = piece
                        self.board[start_y][start_x] = None


                elif piece.color != self.board[end_y][end_x].color:
                    if piece.beat(start, end, self.board[end_y][end_x]):
                        self.board[end_y][end_x] = piece
                        self.board[start_y][start_x] = None
                        return
                else:
                    print("Pieces have the same color")
            else:
                print("It is not your Turn, it is other color's Turn")


c = ChessBoard()
c.display()


def is_valid_input_format(position):
    if len(position) != 2:
        return False
    if ord(position[0].lower()) not in range(97, 105):  # ASCII value of 'a' to 'h'
        return False
    if not position[1].isdigit() or int(position[1]) not in range(1, 9):
        return False
    return True


while True:
    start_pos = input("Enter your starting position (e.g. e2): ")
    end_pos = input("Enter your ending position (e.g. e4): ")

    if start_pos == end_pos:
        print("You didn't make a move.")
        print("  ")
        continue
    if start_pos == "":
        print("You didnt put a value in starting position")
        print("  ")
        continue
    if end_pos == "":
        print("You didnt put a value in ending position")
        print("  ")
        continue
    if not is_valid_input_format(start_pos) or not is_valid_input_format(end_pos):
        print("Invalid input format. Please enter in the format e.g. e2")
        print("  ")
        continue

    c.make_move(start_pos, end_pos)
    c.display()
