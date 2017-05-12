from .piece import Piece

class Bishop(Piece):
    def __init__(self, board, pos, color):
        super().__init__(board, pos, color)
        self.symbol = '♝'
        self.move_dirs = [[1,1],[1,-1],[-1,1],[-1,-1]]

    def moves(self):
        return super().slide_moves(self.move_dirs)
