from .piece import Piece

class Knight(Piece):
    def __init__(self, board, pos, color):
        super().__init__(board, pos, color)
        self.symbol = '♞'
        self.move_dirs = [
            [1,2],
            [2,1],
            [-2,1],
            [-1,2],
            [1,-2],
            [2,-1],
            [-2,-1],
            [-1,-2]
        ]
        self.value = 3

    def moves(self):
        return super().step_moves(self.move_dirs)
