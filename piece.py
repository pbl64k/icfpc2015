from utils import *

class Piece(object):
    def __init__(self, proto, pos, rot = 0):
        self.p = proto
        self.pos = pos
        self.r = rot

    def coords(self):
        for pos in self.p.mems[self.r]:
            yield untranslate(add(pos, self.pos))

    def move(self, b, dpos, r):
        np = Piece(self.p, add(self.pos, dpos), (self.r + r) % len(self.p.mems))
        if np.validp(b):
            return True, np
        else:
            return False, self

    def validp(self, b):
        return all(map(lambda x: b.validp(x), self.coords()))

    def id(self):
        return self.pos, self.r

