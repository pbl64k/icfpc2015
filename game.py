import math

from piece import *
from ui import *

class Game(object):
    def __init__(self, id, pieces, board, lcg):
        self.id = id
        self.pcs = pieces
        self.b = board
        self.lcg = lcg
        self.piece = None
        self.banned = set()
        self.score = 0
        self.ls_old = 0
        self.spawn()

    # mind the slightly weird behavior here:
    # locking takes precedence over the move being "invalid"
    def move(self, m):
        f, pc = self.piece.move(self.b, m[0], m[1])
        if f:
            if pc.id() in self.banned:
                self.score = 0
                return False
            self.piece = pc
            self.banned.add(pc.id())
        else:
            self.b.merge(pc)
            remd = self.b.nuke()
            pts = len(self.piece.p.mems[0]) + int(math.floor(100 * (1 + remd) * (remd / 2.0)))
            bonus = 0 if self.ls_old == 0 else (((self.ls_old - 1) * pts) / 10)
            sc = pts + bonus
            self.score += sc
            self.ls_old = remd
            self.piece = None
            self.spawn()
        return True

    def spawn(self):
        assert self.piece is None
        ix = self.lcg.gen()
        piece = self.pcs[ix % len(self.pcs)]
        sz = piece.max_x - piece.min_x
        off = (self.b.w - sz) / 2
        self.piece = Piece(piece, (off - piece.min_x - 1, -piece.min_y))
        self.banned = set([self.piece.id()])

    def repr(self):
        r = self.b.repr()
        if self.piece is not None:
            pos = untranslate(self.piece.pos)
            if self.b.validp(pos):
                r[pos[1]][pos[0]] = '+'
            for x, y in self.piece.coords():
                if r[y][x] == '+':
                    r[y][x] = '0'
                else:
                    r[y][x] = 'O'
        return r

    def display(self):
        print self.piece.id()
        print self.banned
        display(self.b.w, self.b.h, self.repr())
        print 'Score:', self.score

