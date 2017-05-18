from .piece import *
from .null_piece import NullPiece

class Pawn(Piece):
    def __init__(self, board, pos, color):
        super().__init__(board, pos, color)
        self.symbol = '♟'
        self.value = 1

    def black_moves(self):
        result = []
        if isinstance(self.board.get(add([1,0],self.pos)), NullPiece):
            result.append(add([1,0],self.pos))
            if isinstance(self.board.get(add([2,0],self.pos)), NullPiece) and self.pos[0] == 1:
                result.append(add([2,0],self.pos))
        if self.board.in_range(add(self.pos, [1,1])):
            if self.board.get(add(self.pos, [1,1])).color == "white":
                result.append(add(self.pos, [1,1]))
            elif self.board.get(add(self.pos, [0,1])).color == "white" and self.board.get(add(self.pos, [0,1])).vulnerable:
                result.append(add(self.pos, [1,1]))
        if self.board.in_range(add(self.pos, [1,-1])):
            if self.board.get(add(self.pos, [1,-1])).color == "white":
                result.append(add(self.pos, [1,-1]))
            elif self.board.get(add(self.pos, [0,-1])).color == "white" and self.board.get(add(self.pos, [0,-1])).vulnerable:
                result.append(add(self.pos, [1,-1]))
        return result

    def white_moves(self):
        result = []
        if isinstance(self.board.get(add([-1,0],self.pos)), NullPiece):
            result.append(add([-1,0],self.pos))
            if isinstance(self.board.get(add([-2,0],self.pos)), NullPiece) and self.pos[0] == 6:
                result.append(add([-2,0],self.pos))
        if self.board.in_range(add(self.pos, [-1,1])):
            if self.board.get(add(self.pos, [-1,1])).color == "black":
                result.append(add(self.pos, [-1,1]))
            elif self.board.get(add(self.pos, [0,1])).color == "black" and self.board.get(add(self.pos, [0,1])).vulnerable:
                result.append(add(self.pos, [-1,1]))
        if self.board.in_range(add(self.pos, [-1,-1])):
            if self.board.get(add(self.pos, [-1,-1])).color == "black":
                result.append(add(self.pos, [-1,-1]))
            elif self.board.get(add(self.pos, [0,-1])).color == "black" and self.board.get(add(self.pos, [0,-1])).vulnerable:
                result.append(add(self.pos, [-1,-1]))
        return result

    def moves(self):
        if self.color == "white":
            return self.white_moves()
        else:
            return self.black_moves()
