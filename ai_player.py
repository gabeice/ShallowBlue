from player import Player
from pieces import opposite_color
from board import Board
import random
import copy

class AIPlayer(Player):
    def __init__(self, color):
        super().__init__(color)
        self.depth = 3

    def own_pieces(self, board):
        result = []
        for i in range(8):
            for j in range(8):
                if board.get([i,j]).color == self.color:
                    result.append([i,j])
        return result

    def opposition_pieces(self, board):
        result = []
        for i in range(8):
            for j in range(8):
                if board.get([i,j]).color == opposite_color(self.color):
                    result.append([i,j])
        return result

    def score(self, board, color):
        result = 0
        for i in range(8):
            for j in range(8):
                piece = board.get([i,j])
                if piece.color == color:
                    result += piece.value
        return result

    def own_score(self, board):
        return self.score(board, self.color)

    def opponent_score(self, board):
        return self.score(board, opposite_color(self.color))

    def available_moves(self, board):
        moves = []
        positions = self.own_pieces(board)
        for position in positions:
            possibilities = board.valid_moves(position)
            for move in possibilities:
                moves.append([position, move])
        return moves

    def best_move(self, board, moves):
        best = moves[0]
        best_value = 0
        for move in moves:
            occupant = board.get(move[1])
            if occupant.color == opposite_color(self.color) and occupant.value > best_value:
                best = move
                best_value = occupant.value
        return best

    def mate_move(self, board, move):
        test_board = Board()
        test_board.board = copy.deepcopy(board.board)
        test_board.move_piece(move[0], move[1])
        return test_board.checkmate(opposite_color(self.color))

    def get_move(self, board, display):
        moves = self.available_moves(board)
        for move in moves:
            if self.mate_move(board, move):
                return move
        else:
            return self.best_move(board, moves)
