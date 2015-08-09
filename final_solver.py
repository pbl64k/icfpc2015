import argparse
import json
import sys
import time

started_on = time.time()

from tag import *

from konstruckt import *

import game

parser = argparse.ArgumentParser(description = 'ICFP Contest 2015 -- team Replete With Abstract Joy solver')

parser.add_argument('--nodebug', action = 'store_true')
parser.add_argument('--deadlines', action = 'store_true')
parser.add_argument('--nosave', action = 'store_true')
parser.add_argument('-t', action = 'store')
parser.add_argument('-f', action = 'append')
parser.add_argument('-p', action = 'append')
# these two are actually ignored. *sigh*
parser.add_argument('-c', action = 'store')
parser.add_argument('-m', action = 'store')

args = parser.parse_args()

if args.t is not None:
    tlimit = float(args.t) * 0.95
    if tlimit <= 0.0:
        sys.exit('Time limit must be strictly positive. To run without time limit, simply omit the -t flag.');
    deadline = started_on + tlimit

if args.p is not None:
    pops = map(lambda x: x.lower(), args.p)
    pops.sort(key = len, reverse = True)
    game.moves = pops + game.moves

if args.f is None:
    sys.exit('No problem filenames specified.')

sols = []

pdl = not args.nodebug or args.deadlines

if pdl:
    print 'Started on:', started_on
    print 'Global dealine:', deadline

fnum = 0
for fn in args.f:
    t = time.time()
    file_deadline = t + ((deadline - t) / (len(args.f) - fnum))
    if pdl:
        print fn, 'deadline:', file_deadline
    snum = 0
    for seeds, game in konstruckt(fn, args.nodebug):
        t = time.time()
        seed_deadline = t + ((file_deadline - t) / (seeds - snum))
        if pdl:
            print fn, 'seed', game.lcg.seed, 'deadline:', seed_deadline
        s = game.solve(seed_deadline)
        sols.append({'problemId': game.id, 'seed': game.lcg.seed, 'tag': curTag + '-' + str(game.id) + '-' + str(game.lcg.seed) + '-' + str(time.time()), 'solution': s})
        snum += 1
    fnum += 1

print json.dumps(sols)

if not args.nosave:
    fn = 'solutions/solution_' + str(game.id) + '.json'
    f = open(fn, 'w+')
    f.write(json.dumps(sols))

