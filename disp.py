import json
import sys

from board import *
from pieceproto import *

f = open(sys.argv[1], 'r')
data = json.loads(f.read())

b = Board(data['width'], data['height'], data['filled'])
b.display()

pcs = map(PieceProto, data['units'])
print pcs

