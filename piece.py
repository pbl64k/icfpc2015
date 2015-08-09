import utils

add = utils.add
untranslate = utils.untranslate

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
            return False, np
        else:
            return True, self

    def validp(self, b):
        #return all(map(lambda x: b.validp(x), self.coords()))
        # OPT
        for pos in self.coords():
            if not b.validp(pos): return False
        return True

    def id(self):
        return self.pos, self.r

