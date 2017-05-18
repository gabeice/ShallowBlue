from .piece import *
from .null_piece import NullPiece

class King(Piece):
    def __init__(self, board, pos, color):
        super().__init__(board, pos, color)
        self.symbol = '♚'
        self.move_dirs = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
            [1,1],
            [1,-1],
            [-1,1],
            [-1,-1]
        ]
        self.value = 0

    def moves(self):
        moves = super().step_moves(self.move_dirs)
        if not self.has_moved:
            if not self.board.get(add(self.pos, [0,3])).has_moved and isinstance(self.board.get(add(self.pos, [0,1])), NullPiece) and isinstance(self.board.get(add(self.pos, [0,2])), NullPiece):
                moves.append(add(self.pos, [0,2]))
            if not self.board.get(add(self.pos, [0,-4])).has_moved and isinstance(self.board.get(add(self.pos, [0,-3])), NullPiece) and isinstance(self.board.get(add(self.pos, [0,-2])), NullPiece) and isinstance(self.board.get(add(self.pos, [0,-1])), NullPiece):
                moves.append(add(self.pos, [0,-2]))
        return moves
