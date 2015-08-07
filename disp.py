import json
import sys

from board import *

f = open(sys.argv[1], 'r')
data = json.loads(f.read())

b = Board(data['width'], data['height'], data['filled'])
b.display()

