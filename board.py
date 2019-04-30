from pieces import *
import copy


def move_two(pos1, pos2):
    return abs(pos1[1] - pos2[1]) == 2


class Board(object):
    def __init__(self):
        self.board = []
        self.men_row(0, "black")
        self.pawn_row(1, "black")
        for i in range(2,6):
            self.empty_row(i)
        self.pawn_row(6, "white")
        self.men_row(7, "white")

    def empty_row(self, line):
        row = []
        for i in range(8):
            row.append(NullPiece(self, [line, i]))
        self.board.append(row)

    def pawn_row(self, line, color):
        row = []
        for i in range(8):
            row.append(Pawn(self, [line, i], color))
        self.board.append(row)

    def men_row(self, line, color):
        self.board.append([
            Rook(self, [line, 0], color),
            Knight(self, [line, 1], color),
            Bishop(self, [line, 2], color),
            Queen(self, [line, 3], color),
            King(self, [line, 4], color),
            Bishop(self, [line, 5], color),
            Knight(self, [line, 6], color),
            Rook(self, [line, 7], color)
        ])

    def get(self, pos):
        if pos == []:
            return NullPiece(self, [0,0])
        else:
            return self.board[pos[0]][pos[1]]

    def behind(self, pos):
        if self.get(pos).color == "white":
            return [pos[0]+1,pos[1]]
        else:
            return [pos[0]-1,pos[1]]

    def castle(self, to_pos, from_pos):
        if to_pos[1] == 6:
            self.move_piece([to_pos[0], 7], [to_pos[0], 5])
        else:
            self.move_piece([to_pos[0], 0], [to_pos[0], 3])

    def move_piece(self, pos1, pos2):
        if not isinstance(self.get(pos1), NullPiece):
            is_empty = isinstance(self.get(pos2), NullPiece)
            self.board[pos2[0]][pos2[1]] = self.get(pos1)
            self.get(pos2).pos = pos2
            self.get(pos2).has_moved = True
            self.board[pos1[0]][pos1[1]] = NullPiece(self, pos1)
            if isinstance(self.get(pos2), Pawn) and abs(pos1[0]-pos2[0]) == 2:
                self.get(pos2).vulnerable = True
            if isinstance(self.get(pos2), Pawn) and is_empty and isinstance(self.get(self.behind(pos2)), Pawn):
                self.board[self.behind(pos2)[0]][self.behind(pos2)[1]] = NullPiece(self, self.behind(pos2))
            if isinstance(self.get(pos2), Pawn) and (pos2[0] == 0 or pos2[0] == 7):
                self.board[pos2[0]][pos2[1]] = Queen(self, pos2, self.get(pos2).color)
            if pos2 == self.king_pos(self.get(pos2).color) and move_two(pos1, pos2):
                self.castle(pos2, pos1)

    def clear_pawn_vulnerabilities(self, color):
        for row in self.board:
            for piece in row:
                if piece.color == color and isinstance(piece, Pawn):
                    piece.vulnerable = False

    def in_range(self, pos):
        return pos[0] in range(8) and pos[1] in range(8)

    def king_pos(self, color):
        for i in range(8):
            for j in range(8):
                if isinstance(self.get([i,j]), King) and self.get([i,j]).color == color:
                    return [i,j]

    def check(self, color):
        moves = []
        for i in range(8):
            for j in range(8):
                if self.get([i,j]).color == opposite_color(color):
                    moves.extend(self.get([i,j]).moves())
        return self.king_pos(color) in moves

    def illegal_castle(self, pos, move):
        if isinstance(self.get(pos), King):
            if abs(pos[1] - move[1]) == 2:
                color = self.get(pos).color
                test_board = Board()
                test_board.board = copy.deepcopy(self.board)
                test_board.move_piece(pos, [pos[0],int((move[1]-pos[1])/2)+pos[1]])
                return test_board.check(color)
            else:
                return False
        else:
            return False

    def valid_moves(self, pos):
        moves = self.get(pos).moves()
        result = []
        for move in moves:
            test_board = Board()
            test_board.board = copy.deepcopy(self.board)
            if not self.illegal_castle(pos, move):
                test_board.move_piece(pos, move)
                if not test_board.check(self.get(pos).color):
                    result.append(move)
        return result

    def checkmate(self, color):
        for i in range(8):
            for j in range(8):
                if self.get([i,j]).color == color and self.valid_moves([i,j]) != []:
                    return False
        else:
            return True

    def over(self):
        return self.checkmate("white") or self.checkmate("black")

    def winner(self):
        if self.checkmate("white"):
            return "black"
        elif self.checkmate("black"):
            return "white"

    def render(self):
        print ("_"*33)
        for row in self.board:
            print ("|", end="")
            for item in row:
                print (" %s |" % (item.symbol), end="")
            print ("\n", end="")
            print ("_"*33)
