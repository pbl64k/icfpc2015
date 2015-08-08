import sys

from konstruckt import *

for g in konstruckt(sys.argv[1]):
    g.b.display()
    
    for pc in g.pcs:
        print pc.min_x, pc.max_x, pc.min_y, pc.max_y
        print pc.mems

    break

