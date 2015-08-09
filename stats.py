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

for x in data:
    #print x
    id = x['problemId']
    if id not in ids:
        ids[id] = {}
    seed = x['seed']
    sc = x['score']
    if seed not in ids[id] or (sc is not None and ((ids[id][seed] is None and sc > 0) or ids[id][seed] < sc)):
        ids[id][seed] = sc
    if sc is None:
        pending.append((id, seed, x['tag']))
    if x['tag'][0:len(tag)] == tag:
        if id not in tag_ids:
            tag_ids[id] = {}
        if seed not in tag_ids[id] or (sc is not None and ((tag_ids[id][seed] is None and sc > 0) or tag_ids[id][seed] < sc)):
            tag_ids[id][seed] = sc

for id in ids:
    print 'Problem', id
    for seed in ids[id]:
        print ids[id][seed],
        if id in tag_ids and seed in tag_ids[id]:
            print '(' + str(tag_ids[id][seed]) + ')',
    print
    print

print '*** PENDING ****'

for x in pending:
    print x

