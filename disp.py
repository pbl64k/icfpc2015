import sys

from konstruckt import *

for g in konstruckt(sys.argv[1]):
    g.b.display()
    print g.b.w, 'x', g.b.h
    
    break

