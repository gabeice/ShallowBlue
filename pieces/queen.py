from .piece import Piece

class Queen(Piece):
    def __init__(self, board, pos, color):
        super().__init__(board, pos, color)
        self.symbol = '♛'
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
        self.value = 9

    def moves(self):
        return super().slide_moves(self.move_dirs)
