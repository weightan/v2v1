import golly as g
import sys
from ortconrule import *
from ortconrule import *
sys.setrecursionlimit(2000)

from random import random

import time

p = set()

cells = g.getcells(g.getrect() )

tile = get_s_from_g(cells)

if len(tile) != 0:

    for ttemp in find_groups_Neumann2(tile):
        chunks = enumerate_connected_regions(ttemp)
        for i in find_all_not_biggest_regions(chunks):
            g.setcell(i[0], i[1], 0)

    time.sleep(0.08) 

    g.run(1)
    g.update()


