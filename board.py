from ui import *

class Board(object):
    def __init__(self, w, h, f):
        self.w = w
        self.h = h
        self.b = [[False for y in range(self.h)] for x in range(self.w)]
        for pos in f:
            self.b[pos['x']][pos['y']] = True

    def repr(self):
        return map(lambda x: map(lambda y: '*' if y else ' ', x), self.b)

    def display(self):
        display(self.w, self.h, self.repr())

    def validp(self, pos):
        x, y = pos
        return x >= 0 and x < self.w and y >= 0 and y < self.h and not self.b[x][y]

    def merge(self, pc):
        for x, y in pc.coords():
            assert not self.b[x][y]
            self.b[x][y] = True

