import sys

from konstruckt import *

# TODO: stuff

while True:
    game.display()
    c = getch()
    f, game = game.move(kmap[c])
    if not f:
        break
game.display()

