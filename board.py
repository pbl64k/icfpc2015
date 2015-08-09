from utils import *
from ui import *

class Board(object):
    def __init__(self, w, h, f, dbg = True):
        self.w = w
        self.h = h
        self.dbg = dbg
        self.nukable = []
        self.brd = [[False for y in range(self.w)] for x in range(self.h)]
        self.fill = [0 for ix in range(self.h)]
        self.tot_parts = self.h
        self.parts = [1 for ix in range(self.h)]
        for pos in f:
            self.set(pos['x'], pos['y'], True)

    def get(self, x, y):
        return self.brd[y][x]

    def set(self, x, y, z):
        self.brd[y][x] = z
        self.fill[y] += 1
        if self.fill[y] == self.w:
            self.nukable.append(y)
        l = self.validp((x - 1, y))
        r = self.validp((x + 1, y))
        if l and r:
            self.tot_parts += 1
            self.parts[y] += 1
        elif not l and not r:
            self.tot_parts -= 1
            self.parts[y] -= 1

    def repr(self):
        return map(lambda x: map(lambda y: '*' if y else ' ', x), self.brd)

    def display(self):
        if self.dbg:
            print display(self.w, self.h, self.repr())

    def validp(self, pos):
        x, y = pos
        return x >= 0 and x < self.w and y >= 0 and y < self.h and not self.get(x, y)

    def merge(self, pc):
        for x, y in pc.coords():
            assert not self.get(x, y)
            self.set(x, y, True)

    def nuke(self):
        remd = 0
        if len(self.nukable) > 0:
            self.nukable.sort(reverse = True)
            while len(self.nukable) > 0:
                remd += 1
                ix = self.nukable.pop()
                self.brd.pop(ix)
                self.brd.insert(0, [False for y in range(self.w)])
                self.fill.pop(ix)
                self.fill.insert(0, 0)
                self.parts.pop(ix)
                self.parts.insert(0, 1)
        return remd

    #def nuke(self):
    #    remd = 0
    #    for ix in range(self.h - 1, -1, -1):
    #        while all(self.brd[ix]):
    #            remd += 1
    #            self.brd.pop(ix)
    #            self.brd.insert(0, [False for y in range(self.w)])
    #            self.fill.pop(ix)
    #            self.fill.insert(0, 0)
    #    return remd

    def calc_connect(self):
        r = 0
        v = set()
        fr = [(self.w / 2, 0)]
        while len(fr) > 0:
            pos = fr.pop()
            if pos in v or not self.validp(pos):
                continue
            v.add(pos)
            r += 1
            for n in ns_hextris(pos):
                fr.append(n)
        return r

    def calc_parts(self):
        r = 0.0
        for ix in range(self.h):
            r *= 0.95
            r += self.parts[ix]
        return r

    def calc_magic(self):
        return list(reversed(map(lambda x: x[0] - x[1], zip(self.fill, self.parts))))

