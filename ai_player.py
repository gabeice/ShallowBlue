from player import Player
from pieces import opposite_color
from board import Board
import random
import copy


def spaces(color, board):
    return [[i, j] for i in range(8) for j in range(8) if board.get([i, j]).color == color]


def pieces(color, board):
    return [board.get(space) for space in spaces(color, board)]


def score(board, color):
    return sum([piece.value for piece in pieces(color, board)])


def available_moves(color, board):
    return [[position, move] for position in pieces(color, board) for move in board.valid_moves(position)]


def best_move(board, moves, color):
    best = moves[0]
    best_value = 0
    for move in moves:
        occupant = board.get(move[1])
        if occupant.color == opposite_color(color) and occupant.value > best_value:
            best = move
            best_value = occupant.value
    return [best, best_value]


def move_value(color, board, move, depth):
    opponent = opposite_color(color)
    value = 0
    occupant = board.get(move[1])
    if occupant.color == opponent:
        value = occupant.value
    new_board = Board()
    new_board.board = copy.deepcopy(board.board)
    new_board.move_piece(move[0], move[1])
    value -= best_move(new_board, available_moves(opponent, new_board), opponent)[1]
    return value


def best_moves(color, board, moves, depth):
    best = -100
    result = []
    for move in moves:
        value = move_value(color, board, move, depth)
        if value > best:
            result = [move]
            best = value
        elif value == best:
            result += [move]
    return result


def mate_move(color, board, move):
    new_board = Board()
    new_board.board = copy.deepcopy(board.board)
    new_board.move_piece(move[0], move[1])
    return new_board.checkmate(opposite_color(color))


class AIPlayer(Player):
    def __init__(self, color):
        super().__init__(color)
        self.depth = 3

    def get_move(self, board, display):
        moves = available_moves(self.color, board)
        mate_moves = [mate_move(self.color, board, move) for move in moves]
        if len(mate_moves) > 0:
            return mate_moves[0]
        else:
            return random.choice(best_moves(self.color, board, moves, self.depth))
