from pieces import opposite_color


def get_from_pos(color, board, display):
    from_pos = []
    while board.get(from_pos).color != color or board.valid_moves(from_pos) == []:
        from_pos = display.get_move()[:]
        if board.get(from_pos).color == opposite_color(color):
            display.print_message("Not your piece")
            display.textfield.refresh()
    display.selection = from_pos
    return from_pos


def get_to_pos(from_pos, board, display):
    to_pos = []
    moves = board.valid_moves(from_pos)
    while to_pos not in moves and to_pos != from_pos:
        to_pos = display.get_move()[:]
        if to_pos not in moves and to_pos != from_pos:
            display.print_message("Not a valid move")
            display.textfield.refresh()
    return to_pos


class Player(object):
    def __init__(self, color):
        self.color = color

    def get_move(self, board, display):
        if not display.terminate:
            from_pos = get_from_pos(self.color, board, display)
            if not display.terminate:
                to_pos = get_to_pos(from_pos, board, display)
                if to_pos == from_pos:
                    display.selection = None
                    display.find(to_pos).refresh()
                    return self.get_move(board, display)
                else:
                    return [from_pos, to_pos]
