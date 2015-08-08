from ui import *

class Board(object):
    def __init__(self, w, h, f):
        self.w = w
        self.h = h
        self.brd = [[False for y in range(self.w)] for x in range(self.h)]
        for pos in f:
            self.set(pos['x'], pos['y'], True)

    def get(self, x, y):
        return self.brd[y][x]

    def set(self, x, y, z):
        self.brd[y][x] = z

    def repr(self):
        return map(lambda x: map(lambda y: '*' if y else ' ', x), self.brd)

    def display(self):
        display(self.w, self.h, self.repr())

    def validp(self, pos):
        x, y = pos
        return x >= 0 and x < self.w and y >= 0 and y < self.h and not self.get(x, y)

    def merge(self, pc):
        for x, y in pc.coords():
            # FIXME it's not really clear what happens when a piece spawn and some of the corresponding cells are already occupied?
            #assert not self.get(x, y)
            self.set(x, y, True)

    def nuke(self):
        remd = 0
        for ix in range(self.h - 1, -1, -1):
            while all(self.brd[ix]):
                remd += 1
                self.brd.pop(ix)
                self.brd.insert(0, [False for y in range(self.w)])
        return remd

