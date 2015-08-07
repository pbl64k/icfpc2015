from piece import *
from ui import *

# TODO exclude repeat positions

class Game(object):
    def __init__(self, id, pieces, board, lcg):
        self.id = id
        self.pcs = pieces
        self.b = board
        self.lcg = lcg
        self.piece = None
        self.banned = set()
        self.score = 0
        self.spawn()

    def spawn(self):
        assert self.piece is None
        ix = self.lcg.gen()
        piece = self.pcs[ix % len(self.pcs)]
        self.piece = Piece(piece, (3, 3))

    def repr(self):
        r = self.b.repr()
        if self.piece is not None:
            pos = untranslate(self.piece.pos)
            r[pos[0]][pos[1]] = '+'
            for x, y in self.piece.coords():
                if r[x][y] == '+':
                    r[x][y] = '0'
                else:
                    r[x][y] = 'O'
        return r

    def display(self):
        display(self.b.w, self.b.h, self.repr())
        print 'Score:', self.score

