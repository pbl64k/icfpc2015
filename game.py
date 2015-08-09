import copy
import math
import time

from piece import *
from ui import *

cmap = { \
    'p': ((-1, 0), 0), \
    '\'': ((-1, 0), 0), \
    '!': ((-1, 0), 0), \
    '.': ((-1, 0), 0), \
    '0': ((-1, 0), 0), \
    '3': ((-1, 0), 0), \
    'b': ((1, 0), 0), \
    'c': ((1, 0), 0), \
    'e': ((1, 0), 0), \
    'f': ((1, 0), 0), \
    'y': ((1, 0), 0), \
    '2': ((1, 0), 0), \
    'a': ((-1, 1), 0), \
    'g': ((-1, 1), 0), \
    'h': ((-1, 1), 0), \
    'i': ((-1, 1), 0), \
    'j': ((-1, 1), 0), \
    '4': ((-1, 1), 0), \
    'l': ((0, 1), 0), \
    'm': ((0, 1), 0), \
    'n': ((0, 1), 0), \
    'o': ((0, 1), 0), \
    ' ': ((0, 1), 0), \
    '5': ((0, 1), 0), \
    'd': ((0, 0), 1), \
    'q': ((0, 0), 1), \
    'r': ((0, 0), 1), \
    'v': ((0, 0), 1), \
    'z': ((0, 0), 1), \
    '1': ((0, 0), 1), \
    'k': ((0, 0), -1), \
    's': ((0, 0), -1), \
    't': ((0, 0), -1), \
    'u': ((0, 0), -1), \
    'w': ((0, 0), -1), \
    'x': ((0, 0), -1), \
    }

moves = ['j', 'l', '.', 'y', 'q', 'x']

class Game(object):
    def __init__(self, id, pieces, board, lcg, sln, dbg = True):
        self.id = id
        self.pcs = pieces
        self.b = board
        self.lcg = lcg
        self.sln = sln
        self.spawned = 0
        self.piece = None
        self.banned = frozenset()
        self.score = 0
        self.ls_old = 0
        self.fail = False
        self.dbg = dbg
        self.spawn()

    def move(self, m):
        """ returns game over, valid, locks, new game state """
        assert not self.fail
        g = copy.copy(self)
        g.lcg = copy.deepcopy(self.lcg)
        locks, pc = g.piece.move(g.b, m[0], m[1])
        if not locks:
            if pc.id() in g.banned:
                g.score = 0
                g.fail = True
                return True, False, locks, g
            g.piece = pc
            g.banned = g.banned | frozenset([pc.id()])
        else:
            g.b = copy.deepcopy(g.b)
            g.b.merge(pc)
            remd = g.b.nuke()
            pts = len(g.piece.p.mems[0]) + int(math.floor(100 * (1 + remd) * (remd / 2.0)))
            bonus = 0 if g.ls_old == 0 else (((g.ls_old - 1) * pts) / 10)
            sc = pts + bonus
            g.score += sc
            g.ls_old = remd
            g.piece = None
            if not g.spawn():
                return True, True, locks, g
        return False, True, locks, g

    def apply_moves(self, mvs):
        g = self
        s = ''
        for c in mvs:
            gameover, valid, locks, g = g.move(cmap[c])
            s += c
            if gameover or locks:
                return s, gameover, valid, locks, g
        return s, gameover, valid, locks, g

    def spawn(self):
        assert self.piece is None
        ix = self.lcg.gen()
        ixx = ix % len(self.pcs)
        piece = self.pcs[ixx]
        sz = piece.max_x - piece.min_x + 1
        off = (self.b.w - sz) / 2
        self.piece = Piece(piece, add(piece.pivot, (off - piece.min_x, -piece.min_y)))
        self.banned = frozenset([self.piece.id()])
        self.spawned += 1
        if self.spawned > self.sln or any(map(lambda x: not self.b.validp(x), self.piece.coords())):
            self.spawned = self.sln + 1
            return False
        return True

    def solve(self, dl):
        g = self
        s = ''
        while g.spawned <= g.sln:
            ss, score, g = g.solve_piece()
            g.display()
            s += ss
            if time.time() >= dl:
                return s
        return s

    # TODO I'm keeping the current crap in terms of connectivity/parts. No reasonable alternative.
    # TODO cutoff on successful phrases if no stuff around?
    # TODO stop looking if clears a row? probably not worth it.
    # TODO different algos: (easy) packing, (med) current BFS, (huge) maximize power (+cutoff, +stop-on-clear)
    # TODO opt?
    def solve_piece(self):
        fr = [('', self)]
        excl = set()
        best = None
        while len(fr) > 0:
            #s, g = fr.pop()
            s, g = fr.pop(0)
            for m in moves:
                m2, gameover, valid, locks, g2 = g.apply_moves(m)
                if not valid:
                    continue
                if locks:
                    g2score = g2.search_score()
                    #if best is None or (g2.score > best[1].score or (g2.score == best[1].score and list(reversed(g2.b.fill)) > list(reversed(best[1].b.fill)))):
                    if best is None or g2score > best[1]:
                        best = (s + m2, g2score, g2)
                else:
                    if g2.piece.id() in excl:
                        continue
                    excl.add(g2.piece.id())
                    fr.append((s + m2, g2))
        return best

    def search_score(self):
        #return self.score, list(reversed(self.b.fill))
        #return self.score, self.b.calc_connect(), list(reversed(self.b.fill))
        return self.score, -self.b.tot_parts, list(reversed(self.b.fill))
        #return self.score, -self.b.calc_parts(), list(reversed(self.b.fill))
        #return self.score, self.b.calc_magic()

    def repr(self):
        r = self.b.repr()
        if self.piece is not None:
            pos = untranslate(self.piece.pos)
            if self.b.validp(pos):
                r[pos[1]][pos[0]] = '+'
            for x, y in self.piece.coords():
                if r[y][x] == '+':
                    r[y][x] = '0'
                else:
                    r[y][x] = 'O'
        return r

    def display(self):
        if self.dbg:
            print
            print display(self.b.w, self.b.h, self.repr())
            print 'Problem', self.id, ('(' + str(self.lcg.seed) + ')')
            #print 'Connectivity:', self.b.calc_connect()
            #print 'Parts:', self.b.parts
            print '*** FAIL! *** Score:' if self.fail else 'Score:', self.score

