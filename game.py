from board import Board
from display import Display
from player import Player
import os

def move_two(pos1, pos2):
    return abs(pos1[1] - pos2[1]) == 2

class Game(object):
    def __init__(self):
        self.board = Board()
        self.player1 = Player("white")
        self.player2 = Player("black")
        self.display = Display(self.board)
        self.current_player = self.player1

    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        self.board.clear_pawn_vulnerabilities(self.current_player.color)

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

    def castle(self, to_pos, from_pos):
        if to_pos[1] == 6:
            self.board.move_piece([to_pos[0], 7], [to_pos[0], 5])
        else:
            self.board.move_piece([to_pos[0], 0], [to_pos[0], 3])

    def play_turn(self):
        self.display.print_message("  %s's turn   " % self.current_player.color)

        from_pos = self.current_player.get_from_pos(self.board, self.display)
        to_pos = self.current_player.get_to_pos(from_pos, self.board, self.display)

        if from_pos == self.board.king_pos(self.current_player.color) and move_two(from_pos, to_pos):
            self.castle(to_pos, from_pos)

        self.board.move_piece(from_pos, to_pos)
        self.display.find(from_pos).refresh()
        self.display.find(to_pos).refresh()
        self.display.find(self.display.selection).refresh()
        self.display.selection = None

test = Game()
test.play()
