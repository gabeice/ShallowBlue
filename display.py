import curses
from board import Board

class Display(object):
    def __init__(self, board):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        self.board = board
        self.pos = [0,0]
        self.selection = None
        self.spaces = [[],[],[],[],[],[],[],[]]
        self.textfield = curses.newwin(3, 8, 24, 0)

        curses.noecho()
        curses.cbreak()
        curses.start_color()

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)

    def print_message(self, message):
        self.textfield.addstr(0, 0, message)

    def set_color(self, square, color):
        self.spaces[square[0]][square[1]].bkgd(curses.color_pair(color))

    def render(self):
        for i in range(8):
            for j in range(8):
                win = curses.newwin(3, 6, i*3, j*6)
                win.addstr(self.board.get([i,j]).letter)
                if [i, j] == self.selection:
                    win.bkgd(curses.color_pair(3))
                elif (i+j)%2 == 0:
                    win.bkgd(curses.color_pair(1))
                win.refresh()
                self.spaces[i].append(win)
        # curses.napms(3000)

    def get_move(self):
        key = None
        self.render()
        if(self.selection):
            self.set_color(self.selection, 3)
        self.set_color(self.pos, 2)
        self.spaces[self.pos[0]][self.pos[1]].refresh()

        while key != '\n':
            key = self.textfield.getkey()
            if key in "ABCD":
                if (self.pos == self.selection):
                    self.set_color(self.pos, 3)
                elif (self.pos[0] + self.pos[1])%2 == 0:
                    self.set_color(self.pos, 1)
                else:
                    self.set_color(self.pos, 0)
                self.spaces[self.pos[0]][self.pos[1]].addstr(0, 0, self.board.get(self.pos).letter)
                self.spaces[self.pos[0]][self.pos[1]].refresh()

                if key == "A":
                    self.pos[0] = (self.pos[0]-1)%8
                elif key == "B":
                    self.pos[0] = (self.pos[0]+1)%8
                elif key == "D":
                    self.pos[1] = (self.pos[1]-1)%8
                else:
                    self.pos[1] = (self.pos[1]+1)%8
                self.set_color(self.pos, 2)
                self.spaces[self.pos[0]][self.pos[1]].addstr(0, 0, self.board.get(self.pos).letter)
                self.spaces[self.pos[0]][self.pos[1]].refresh()

        # if (selection[0] + selection[1])%2 == 0:
        #     self.spaces[selection[0]][selection[1]].bkgd(curses.color_pair(1))
        # else:
        #     self.spaces[selection[0]][selection[1]].bkgd(curses.color_pair(0))
        #     self.spaces[selection[0]][selection[1]].refresh()
        #     selection = self.pos[:]
        #     self.spaces[selection[0]][selection[1]].bkgd(curses.color_pair(3))
        #     self.spaces[selection[0]][selection[1]].refresh()

        return self.pos


    def close(self):
        self.screen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

# test_board = Board()
# test = Display(test_board)
# selection = str(test.get_move())
# test.close()
# print (selection)
