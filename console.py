import json
import sys

from getch import *

from board import *
from game import *
from lcg import *
from pieceproto import *
from ui import *

f = open(sys.argv[1], 'r')
data = json.loads(f.read())

b = Board(data['width'], data['height'], data['filled'])
pcs = map(PieceProto, data['units'])
lcg = Lcg(data['sourceSeeds'][0])
game = Game(None, pcs, b, lcg, data['sourceLength'])

kmap = {'u': ((-1, 0), 0), \
    'i': ((0, 0), 1), \
    'o': ((1, 0), 0), \
    'j': ((-1, 1), 0), \
    'k': ((0, 0), -1), \
    'l': ((0, 1), 0), \
    }

while True:
    game.display()
    c = getch()
    f, game = game.move(kmap[c])
    if not f:
        break
game.display()

