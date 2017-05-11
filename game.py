from board import Board
import os

class Game(object):
    def __init__(self):
        self.board = Board()
        self.turn = "white"

    def switch_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def play(self):
        while not self.board.over():
            self.play_turn()
            self.switch_turn()

    def play_turn(self):
        from_pos = []
        while self.board.get(from_pos).color != self.turn:
            os.system("clear")
            self.board.render()
            from_pos = input("%s's turn to move. Pick a square to move from: " % (self.turn))
            from_pos = [int(num) for num in from_pos.split(",")]

        to_pos = []
        while to_pos not in self.board.valid_moves(from_pos):
            os.system("clear")
            self.board.render()
            to_pos = input("Pick a square to move to: ")
            to_pos = [int(num) for num in to_pos.split(",")]

        self.board.move_piece(from_pos, to_pos)

test = Game()
test.play()
