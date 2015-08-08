from ui import *

class Board(object):
    def __init__(self, w, h, f, dbg = True):
        self.w = w
        self.h = h
        self.dbg = dbg
        self.brd = [[False for y in range(self.w)] for x in range(self.h)]
        self.fill = [0 for ix in range(self.h)]
        for pos in f:
            self.set(pos['x'], pos['y'], True)

    def get(self, x, y):
        return self.brd[y][x]

    def set(self, x, y, z):
        self.brd[y][x] = z
        self.fill[y] += 1

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
        for ix in range(self.h - 1, -1, -1):
            while all(self.brd[ix]):
                remd += 1
                self.brd.pop(ix)
                self.brd.insert(0, [False for y in range(self.w)])
                self.fill.pop(ix)
                self.fill.insert(0, 0)
        return remd

