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

