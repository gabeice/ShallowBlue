from board import Board
from display import Display
import os

class Game(object):
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.display = Display(self.board)

    def switch_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def play(self):
        while not self.board.over():
            self.play_turn()
            self.switch_turn()
        else:
            self.display.close()

    def play_turn(self):
        from_pos = []
        while self.board.get(from_pos).color != self.turn:
            from_pos = self.display.get_move()[:]
        self.display.selection = from_pos

        to_pos = []
        while to_pos not in self.board.valid_moves(from_pos):
            to_pos = self.display.get_move()[:]

        self.board.move_piece(from_pos, to_pos)
        self.display.find(from_pos).refresh()
        self.display.find(to_pos).refresh()
        self.display.find(self.display.selection).refresh()
        self.display.selection = None

test = Game()
test.play()
