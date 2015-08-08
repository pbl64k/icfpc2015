import sys

from getch import *

from konstruckt import *

kmap = {'u': ((-1, 0), 0), \
    'i': ((0, 0), 1), \
    'o': ((1, 0), 0), \
    'j': ((-1, 1), 0), \
    'k': ((0, 0), -1), \
    'l': ((0, 1), 0), \
    }

for game in konstruckt(sys.argv[1]):
    while True:
        game.display()
        c = getch()
        f, game = game.move(kmap[c])
        if not f:
            break
    game.display()
    break

