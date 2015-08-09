import json
import sys
import time

from tag import *

from konstruckt import *

save = True

sols = []

for game in konstruckt(sys.argv[1]):
    s = game.solve()
    sols.append({'problemId': game.id, 'seed': game.lcg.seed, 'tag': curTag + '-' + str(game.id) + '-' + str(game.lcg.seed) + '-' + str(time.time()), 'solution': s})

print json.dumps(sols)

if save:
    fn = 'solutions/solution_' + str(game.id) + '.json'
    f = open(fn, 'w+')
    f.write(json.dumps(sols))

