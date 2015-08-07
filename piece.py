from utils import *

class Piece(object):
    def __init__(self, proto, pos):
        self.p = proto
        self.pos = pos
        self.r = 0

    def w(self):
        self.pos = sub(self.pos, (1, 0))

    def e(self):
        self.pos = add(self.pos, (1, 0))

    def sw(self):
        self.pos = add(self.pos, (-1, 1))

    def se(self):
        self.pos = add(self.pos, (0, 1))

    def cw(self):
        self.r = (self.r + 1) % len(self.p.mems)

    def ccw(self):
        self.r = (self.r - 1) % len(self.p.mems)

