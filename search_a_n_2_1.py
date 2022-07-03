import golly as g
import sys
from random import random
import time
from ortconrule import *
sys.setrecursionlimit(2000)

def save_osc(s):
    g.save(s + '.rle', 'rle')

found_ones = set()

def search_period(its):
    g.select([0,0,1,1,])
    g.clear(1)
    Rsq = 8
    pop = (Rsq**2)/2

    for i in range(Rsq):
        for j in range(Rsq):
            g.setcell(i, j, 1 if random() < pop/(Rsq**2) else 0)

    p = set()
    q = [(-1, -1, -1) for i in range(200)]
    number_of_mem = len(q)

    found = 0


    for i in range(its):
        cells = g.getcells(g.getrect() )
        tile = get_s_from_g(cells)

        if len(cells)//2 > 240:
            break

        tcells = cells.copy()

        ox = tcells[0]
        oy = tcells[1]

        for i in range(0, len(tcells)):
            if i%2 == 0:
                tcells[i] = tcells[i] - ox
            else:
                tcells[i] = tcells[i] - oy

        if q[-1][2] == tcells:
            #g.show('still life')
            signature = f'still life {len(tcells)//2};{g.getrect()[2:]}  '
            
            if signature not in found_ones:
                found+=1
                found_ones.add(signature)
                #save_osc(signature)  
            break

        else:
            c = 0
            for j in range(2, number_of_mem):


                if q[-j][2] == tcells:


                    minpopul = len(min(q[-j:], key = lambda item: len(item[2]))[2])

                    if q[-j][0] == ox and q[-j][1] == oy:
                        #break

                        signature = f'p{j} osc {minpopul}'

                        if signature not in found_ones:
                            found+=1
                            found_ones.add(signature)
                            save_osc(signature)
                            

                    else:

                        dx = int(abs(ox - q[-j][0]))
                        dy = int(abs(oy - q[-j][1]))

                        signature = f'p{j} ship{dx+dy};{minpopul};{max(dx,dy)};{min(dx,dy)};'
                        #signature = f'p{j} ship {max(dx,dy)};{min(dx,dy)};'

                        if signature not in found_ones:
                            found+=1
                            found_ones.add(signature)
                            save_osc(signature)
                    c = 1
                    break
            if c == 1:
                break
            q.append((ox, oy, tcells))


        if len(q) > number_of_mem:
            q = q[1:]

        if len(tile) != 0:

            for ttemp in find_groups_Neumann2(tile):
                chunks = enumerate_connected_regions(ttemp)
                for i in find_all_not_biggest_regions(chunks):
                    g.setcell(i[0], i[1], 0)


            #time.sleep(0.04) 

            g.run(1)
            
            #g.update()

            if int(g.getpop()) == 0:
                #g.show(f'death')
                break

    return found

            


K = 50000
foundk = 0

g.show('start')
for i in range(K):
    foundk += search_period(200)
    g.show(f'i: {i}')
    
data = f'r: {g.getrule()} iters: {K}, new: {foundk}'


with open('slogfile.txt', 'a') as f:
    print(data, file=f)

    # g.show(f' I: {i}')
g.show(f'done')