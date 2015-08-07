
class Board(object):
    def __init__(self, w, h, f):
        self.w = w
        self.h = h
        self.b = [[False for y in range(self.h)] for x in range(self.w)]
        for pos in f:
            self.b[pos['x']][pos['y']] = True

    def display(self):
        f = False
        l = ''
        for y in range(self.h):
            if f: l += ' '
            f = not f
            l += '|'
            for x in range(self.w):
                if self.b[x][y]:
                    l += '*'
                else:
                    l += ' '
                l += '|'
            l += '\n'
        print l

