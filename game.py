
import copy

class Game(object):
    def __init__(self, id, units, board, lcg):
        self.id = id
        self.units = units
        self.b = board
        self.lcg = lcg
        self.unit = None
        self.banned = set()
        self.score = 0

    def spawn(self):
        assert self.unit is None
        self.unit = Piece(self.units[lcg.gen()])

