import copy
import json
import sys

if len(sys.argv) > 1:
    tag = sys.argv[1]
else:
    tag = 'NONSENSE'

f = open('sols.txt', 'r')
data = json.loads(f.read())

ids = {}
tag_ids = {}
pending = []
best = {}

for x in data:
    id = x['problemId']
    if id not in ids:
        ids[id] = {}
        best[id] = {}
    seed = x['seed']
    sc = x['score']
    if seed not in ids[id] or (sc is not None and ((ids[id][seed] is None and sc > 0) or ids[id][seed] < sc)):
        ids[id][seed] = sc
        best[id][seed] = x
    if sc is None:
        pending.append((id, seed, x['tag']))
    if x['tag'][0:len(tag)] == tag:
        if id not in tag_ids:
            tag_ids[id] = {}
        if seed not in tag_ids[id] or (sc is not None and ((tag_ids[id][seed] is None and sc > 0) or tag_ids[id][seed] < sc)):
            tag_ids[id][seed] = sc

ps = []

bestl = []

for id in ids:
    print 'Problem', id
    bsum = 0.0
    ssum = 0.0
    for seed in ids[id]:
        b = copy.deepcopy(best[id][seed])
        b['tag'] = 'BEST:' + str(b['tag'])
        bestl.append(b)
        print ids[id][seed],
        bsum += ids[id][seed]
        if id in tag_ids and seed in tag_ids[id]:
            print '(' + str(tag_ids[id][seed]) + ')',
            ssum += tag_ids[id][seed]
    n = len(ids[id])
    print
    print 'Average:', (bsum / n), ('' if ssum == 0.0 else ('(' + str(ssum / n) + ')'))
    if ssum > 0.0:
        p = ssum / bsum * 100
        print 'Percentage:', ('%.1f%%' % p)
        ps.append(p)
    print

if len(ps) > 0:
    print 'PERCENTAGE:', ('%.1f%%' % (sum(ps) / len(ps)))
    print

print '*** PENDING ****'

for x in pending:
    print x

ff = open('best.txt', 'w')
ff.write(json.dumps(bestl))

