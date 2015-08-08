import json

f = open('sols.txt', 'r')
data = json.loads(f.read())

ids = {}
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

for id in ids:
    print 'Problem', id
    for seed in ids[id]:
        print ids[id][seed],
    print
    print

print '*** PENDING ****'

for x in pending:
    print x

