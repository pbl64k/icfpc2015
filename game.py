import copy
import math

from piece import *
from ui import *

class Game(object):
    def __init__(self, id, pieces, board, lcg, sln):
        self.id = id
        self.pcs = pieces
        self.b = board
        self.lcg = lcg
        self.sln = sln
        self.spawned = 0
        self.piece = None
        self.banned = frozenset()
        self.score = 0
        self.ls_old = 0
        self.spawn()

    # FIXME? mind the slightly weird behavior here:
    # locking takes precedence over the move being "invalid"
    def move(self, m):
        g = copy.copy(self)
        f, pc = g.piece.move(g.b, m[0], m[1])
        if f:
            if pc.id() in g.banned:
                g.score = 0
                return False, g
            g.piece = pc
            g.banned = g.banned | frozenset(pc.id())
        else:
            g.b = copy.copy(g.b)
            g.b.merge(pc)
            remd = g.b.nuke()
            pts = len(g.piece.p.mems[0]) + int(math.floor(100 * (1 + remd) * (remd / 2.0)))
            bonus = 0 if g.ls_old == 0 else (((g.ls_old - 1) * pts) / 10)
            sc = pts + bonus
            g.score += sc
            g.ls_old = remd
            g.piece = None
            if not g.spawn():
                return False, g
        return True, g

    def spawn(self):
        assert self.piece is None
        ix = self.lcg.gen()
        piece = self.pcs[ix % len(self.pcs)]
        sz = piece.max_x - piece.min_x
        off = (self.b.w - sz) / 2
        self.piece = Piece(piece, (off - piece.min_x - 1, -piece.min_y))
        self.banned = frozenset([self.piece.id()])
        self.spawned += 1
        if self.spawned > self.sln:
            return False
        return True

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

