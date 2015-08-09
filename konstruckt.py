import json

from board import *
from game import *
from lcg import *
from pieceproto import *

def konstruckt(fn, nodebug = False):
    f = open(fn, 'r')
    data = json.loads(f.read())
    
    b = Board(data['width'], data['height'], data['filled'])
    pcs = map(PieceProto, data['units'])
    for ss in data['sourceSeeds']:
        lcg = Lcg(ss)
        game = Game(data['id'], pcs, b, lcg, data['sourceLength'], not nodebug)
        yield game

