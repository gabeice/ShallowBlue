from .piece import Piece

class NullPiece(Piece):
    def __init__(self, board, pos):
        super().__init__(board, pos, None)
        self.symbol = " "
