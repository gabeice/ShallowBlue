def add(pos1, pos2):
    return [pos1[0] + pos2[0], pos1[1] + pos2[1]]

def opposite_color(color):
    if color == "white":
        return "black"
    else:
        return "white"

class Piece(object):
    def __init__(self, board, pos, color):
        self.board = board
        self.pos = pos
        self.original_pos = pos
        self.color = color
        self.has_moved = False
        self.vulnerable = False

    def step_moves(self, dirs):
        return [add(move, self.pos) for move in dirs if self.board.in_range(add(move, self.pos)) and self.board.get(add(move, self.pos)).color != self.color]

    def slide_moves(self, dirs):
        result = []
        for move in dirs:
            result.append(add(self.pos, move))
            while True:
                if not self.board.in_range(result[-1]):
                    result.pop()
                    break
                elif self.board.get(result[-1]).color == self.color:
                    result.pop()
                    break
                elif self.board.get(result[-1]).color == opposite_color(self.color):
                    break
                else:
                    result.append(add(result[-1], move))
        return result
