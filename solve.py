import json
import sys
import time

from konstruckt import *

sols = []

for game in konstruckt(sys.argv[1]):
    s = game.solve()
    sols.append({'problemId': game.id, 'seed': game.lcg.seed, 'tag': str(time.time()), 'solution': s})

print json.dumps(sols)

