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

    def opponent_available_moves(self, board):
        moves = []
        positions = self.opposition_pieces(board)
        for position in positions:
            possibilities = board.valid_moves(position)
            for move in possibilities:
                moves.append([position, move])
        return moves

    def move_value(self, board, move):
        value = 0
        occupant = board.get(move[1])
        if occupant.color == opposite_color(self.color):
            value = occupant.value
        new_board = Board()
        new_board.board = copy.deepcopy(board.board)
        new_board.move_piece(move[0], move[1])
        value -= self.best_move(new_board, self.opponent_available_moves(new_board), opposite_color(self.color))[1]
        return value

    def best_move(self, board, moves, color):
        best = moves[0]
        best_value = 0
        for move in moves:
            occupant = board.get(move[1])
            if occupant.color == opposite_color(color) and occupant.value > best_value:
                best = move
                best_value = occupant.value
        return [best, best_value]

    def best_moves(self, board, moves):
        best = -100
        result = []
        for move in moves:
            value = self.move_value(board, move)
            if value > best:
                result = [move]
                best = value
            elif value == best:
                result += [move]
        return result

    def mate_move(self, board, move):
        new_board = Board()
        new_board.board = copy.deepcopy(board.board)
        new_board.move_piece(move[0], move[1])
        return new_board.checkmate(opposite_color(self.color))

    def get_move(self, board, display):
        moves = self.available_moves(board)
        for move in moves:
            if self.mate_move(board, move):
                return move
        else:
            best = self.best_moves(board, moves)
            return random.choice(best)
