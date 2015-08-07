class Game(object):
    def __init__(self, id, pieces, board, lcg):
        self.id = id
        self.pcs = pieces
        self.b = board
        self.lcg = lcg
        self.piece = None
        self.banned = set()
        self.score = 0

    def repr(self):
        r = self.b.repr()
        if self.piece is not None:
            r[self.piece.pos[0]][self.piece.pos[1]] = '+'
            for x, y in self.piece.coords():
                if r[x][y] == '+':
                    r[x][y] = '0'
                else:
                    r[x][y] = 'O'
        return r

    def display(self):
        display(self.b.w, self.b.h, self.repr())
