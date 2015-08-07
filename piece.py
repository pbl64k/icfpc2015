from utils import *

class Piece(object):
    def __init__(self, proto, pos):
        self.p = proto
        self.pos = pos
        self.r = 0

    def coords(self):
        for pos in self.p.mems[self.r]:
            yield untranslate(add(pos, self.pos))

    def move(self, dpos, r):
        self.pos = add(self.pos, dpos)
        self.r = (self.r + r) % len(self.p.mems)

    def w(self):
        self.move((-1, 0), 0)

    def e(self):
        self.move((1, 0), 0)

    def sw(self):
        self.move((-1, 1), 0)

    def se(self):
        self.move((0, 1), 0)

    def cw(self):
        self.move((0, 0), 1)

    def ccw(self):
        self.move((0, 0), -1)

