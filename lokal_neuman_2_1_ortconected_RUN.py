import golly as g
import sys
from ortconrule import *
from ortconrule import *
sys.setrecursionlimit(2000)

from random import random

import time

p = set()
# g.show('press 0 to stop')
for i in range(1000):
    # ev = g.getevent()

    # if ev == "key m none":
    #     break

    cells = g.getcells(g.getrect() )

    if len(cells)//2 > 2400:
        break

    tile = get_s_from_g(cells)

    if tile == p:
        break
    else:
        p = tile.copy()

    if len(tile) != 0:

        for ttemp in find_groups_Neumann2(tile):
            chunks = enumerate_connected_regions(ttemp)
            for i in find_all_not_biggest_regions(chunks):
                g.setcell(i[0], i[1], 0)

        time.sleep(0.08) 

        g.run(1)
        g.update()

        if int(g.getpop()) == 0:
            break
