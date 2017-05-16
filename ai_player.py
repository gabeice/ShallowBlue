from player import Player
from pieces import opposite_color
import random
from board import Board

class AIPlayer(Player):
    def __init__(self, color):
        super().__init__(color)
        self.depth = 5

    def own_pieces(self, board):
        result = []
        for i in range(8):
            for j in range(8):
                if board.get([i,j]).color == self.color:
                    result.append([i,j])
        return result

    def available_moves(self, board):
        moves = []
        positions = self.own_pieces(board)
        for position in positions:
            possibilities = board.valid_moves(position)
            for move in possibilities:
                moves.append([position, move])
        return moves

    def get_move(self, board, display):
        moves = self.available_moves(board)
        return random.choice(moves)
