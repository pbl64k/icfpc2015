import argparse
import json
import sys
import time

from tag import *

from konstruckt import *

import game

parser = argparse.ArgumentParser(description = 'ICFP Contest 2015 -- team Replete With Abstract Joy solver')

parser.add_argument('--nodebug', action = 'store_true')
parser.add_argument('--nosave', action = 'store_true')
parser.add_argument('-t', action = 'store')
parser.add_argument('-f', action = 'append')
parser.add_argument('-p', action = 'append')
# these two are actually ignored. *sigh*
parser.add_argument('-c', action = 'store')
parser.add_argument('-m', action = 'store')

args = parser.parse_args()

if args.f is None:
    sys.exit('No problem filenames specified.')

if args.p is not None:
    pops = map(lambda x: x.lower(), args.p)
    pops.sort(key = len, reverse = True)
    game.moves = pops + game.moves

sols = []

for fn in args.f:
    for game in konstruckt(fn, args.nodebug):
        s = game.solve()
        sols.append({'problemId': game.id, 'seed': game.lcg.seed, 'tag': curTag + '-' + str(game.id) + '-' + str(game.lcg.seed) + '-' + str(time.time()), 'solution': s})

print json.dumps(sols)

if not args.nosave:
    fn = 'solutions/solution_' + str(game.id) + '.json'
    f = open(fn, 'w+')
    f.write(json.dumps(sols))

