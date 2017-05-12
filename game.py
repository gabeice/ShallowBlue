from board import Board
from display import Display
import os
from pieces import opposite_color

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
            self.display.render()
            self.display.print_message("%s wins!   " % self.board.winner())
            self.display.textfield.refresh()
            self.display.sleep(2000)
            self.display.close()

    def play_turn(self):
        self.display.print_message("  %s's turn   " % self.turn)

        from_pos = []
        while self.board.get(from_pos).color != self.turn:
            from_pos = self.display.get_move()[:]
            if self.board.get(from_pos).color == opposite_color(self.turn):
                self.display.print_message("Not your piece")
                self.display.textfield.refresh()
        self.display.selection = from_pos

        to_pos = []
        while to_pos not in self.board.valid_moves(from_pos):
            to_pos = self.display.get_move()[:]
            if to_pos not in self.board.valid_moves(from_pos):
                self.display.print_message("Not a valid move")
                self.display.textfield.refresh()

        self.board.move_piece(from_pos, to_pos)
        self.display.find(from_pos).refresh()
        self.display.find(to_pos).refresh()
        self.display.find(self.display.selection).refresh()
        self.display.selection = None

test = Game()
test.play()
