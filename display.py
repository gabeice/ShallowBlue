import curses

class Display(object):
    def __init__(self, board):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        self.board = board
        self.pos = [0,0]
        self.selection = None
        self.spaces = [[],[],[],[],[],[],[],[]]
        self.textfield = curses.newwin(3, 18, 24, 0)

        curses.noecho()
        curses.cbreak()
        curses.start_color()

        curses.init_color(3, 139, 69, 19)
        curses.init_color(4, 245, 222, 179)

        curses.init_pair(1, curses.COLOR_BLACK, 4)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(4, curses.COLOR_BLACK, 3)

        curses.init_pair(5, curses.COLOR_WHITE, 4)
        curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_RED)
        curses.init_pair(8, curses.COLOR_WHITE, 3)

    def print_message(self, message):
        self.textfield.addstr(0, 0, message)

    def find(self, square):
        return self.spaces[square[0]][square[1]]

    def set_color(self, square, color):
        if self.board.get(square).color == "black":
            self.find(square).bkgd(curses.color_pair(color))
        else:
            self.find(square).bkgd(curses.color_pair(color+4))

    def render(self):
        self.spaces = [[],[],[],[],[],[],[],[]]
        for i in range(8):
            for j in range(8):
                win = curses.newwin(3, 6, i*3, j*6)
                win.addstr(1, 2, self.board.get([i,j]).letter)
                self.spaces[i].append(win)
                if [i, j] == self.selection:
                    self.set_color([i, j], 3)
                elif (i+j)%2 == 0:
                    self.set_color([i, j], 1)
                else:
                    self.set_color([i, j], 4)
                win.refresh()

    def get_move(self):
        key = None
        self.render()
        self.set_color(self.pos, 2)
        if(self.selection):
            self.set_color(self.selection, 3)
        self.find(self.pos).addstr(1, 2, self.board.get(self.pos).letter)
        self.find(self.pos).refresh()

        while key != '\n':
            key = self.textfield.getkey()
            if key in "ABCD":
                if (self.pos == self.selection):
                    self.set_color(self.pos, 3)
                elif (self.pos[0] + self.pos[1])%2 == 0:
                    self.set_color(self.pos, 1)
                else:
                    self.set_color(self.pos, 4)
                self.find(self.pos).addstr(1, 2, self.board.get(self.pos).letter)
                self.find(self.pos).refresh()

                if key == "A":
                    self.pos[0] = (self.pos[0]-1)%8
                elif key == "B":
                    self.pos[0] = (self.pos[0]+1)%8
                elif key == "D":
                    self.pos[1] = (self.pos[1]-1)%8
                else:
                    self.pos[1] = (self.pos[1]+1)%8
                self.set_color(self.pos, 2)
                self.find(self.pos).addstr(1, 2, self.board.get(self.pos).letter)
                self.find(self.pos).refresh()
            self.textfield.addstr(0,0, "")

        return self.pos

    def close(self):
        self.screen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
