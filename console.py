import json
import sys

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
game = Game(None, pcs, b, lcg)
game.display()

