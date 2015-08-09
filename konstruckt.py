import json

from debug import *

from board import *
from game import *
from lcg import *
from pieceproto import *

def konstruckt(fn):
    f = open(fn, 'r')
    data = json.loads(f.read())
    
    b = Board(data['width'], data['height'], data['filled'])
    pcs = map(PieceProto, data['units'])
    for ss in data['sourceSeeds']:
        lcg = Lcg(ss)
        game = Game(data['id'], pcs, b, lcg, data['sourceLength'], debug)
        yield game

