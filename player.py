from pieces import opposite_color

class Player(object):
    def __init__(self, color):
        self.color = color

    def get_from_pos(self, board, display):
        from_pos = []
        while board.get(from_pos).color != self.color or board.valid_moves(from_pos) == []:
            from_pos = display.get_move()[:]
            if board.get(from_pos).color == opposite_color(self.color):
                display.print_message("Not your piece")
                display.textfield.refresh()
        display.selection = from_pos
        return from_pos

    def get_to_pos(self, from_pos, board, display):
        to_pos = []
        while to_pos not in board.valid_moves(from_pos):
            to_pos = display.get_move()[:]
            if to_pos not in board.valid_moves(from_pos):
                display.print_message("Not a valid move")
                display.textfield.refresh()
        return to_pos
