import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
stdscr.keypad(True)
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)

pos = [0,0]
key = None
selection = [1,1]
spaces = [[],[],[],[],[],[],[],[]]

for i in range(8):
    for j in range(8):
        win = curses.newwin(3, 6, i*3, j*6)
        win.addstr(" ")
        if (i+j)%2 == 0:
            win.bkgd(curses.color_pair(1))
        win.refresh()
        spaces[i].append(win)

textfield = curses.newwin(3, 8, 24, 0)

spaces[0][0].bkgd(curses.color_pair(2))
spaces[0][0].refresh()

while key != 'q':
    key = textfield.getkey()
    if key in "ABCD":
        if (pos == selection):
            spaces[pos[0]][pos[1]].bkgd(curses.color_pair(3))
        elif (pos[0] + pos[1])%2 == 0:
            spaces[pos[0]][pos[1]].bkgd(curses.color_pair(1))
        else:
            spaces[pos[0]][pos[1]].bkgd(curses.color_pair(0))
        spaces[pos[0]][pos[1]].refresh()
        if key == "A":
            pos[0] = (pos[0]-1)%8
        elif key == "B":
            pos[0] = (pos[0]+1)%8
        elif key == "D":
            pos[1] = (pos[1]-1)%8
        else:
            pos[1] = (pos[1]+1)%8
        spaces[pos[0]][pos[1]].bkgd(curses.color_pair(2))
        spaces[pos[0]][pos[1]].refresh()

    elif key == "\n":
        if (selection[0] + selection[1])%2 == 0:
            spaces[selection[0]][selection[1]].bkgd(curses.color_pair(1))
        else:
            spaces[selection[0]][selection[1]].bkgd(curses.color_pair(0))
        spaces[selection[0]][selection[1]].refresh()
        selection = pos[:]
        spaces[selection[0]][selection[1]].bkgd(curses.color_pair(3))
        spaces[selection[0]][selection[1]].refresh()

    textfield.addstr(0, 0, str(pos))

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
