import sys

from konstruckt import *

for g in konstruckt(sys.argv[1]):
    g.b.display()
    print g.b.w, 'x', g.b.h
    
    #for pc in g.pcs:
    #    print pc.min_x, pc.max_x, pc.min_y, pc.max_y
    #    print pc.mems

    break

