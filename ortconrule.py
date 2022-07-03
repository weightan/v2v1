def get_s_from_g(s):
    out = set()
    for i in range(0,len(s),2):
        out.add((s[i], s[i+1]))
    return out

def connected_tile(k):
    s = k.copy()
    def near(x,y):
        return ((x,y+1),(x+1,y),(x-1,y),(x,y-1),)

    def start_from_seed(x,y):
        if (x,y) not in s:
            return
        s.discard((x,y))
        for dx, dy in near(x, y):
            start_from_seed(dx, dy)
    start_from_seed(*tuple(s)[0])
    return len(s) == 0

def enumerate_connected_regions(k):
    s = k.copy()
    def near(x,y):
        return ((x,y+1),(x+1,y),(x-1,y),(x,y-1),)
    def start_from_seed(x,y):
        if (x,y) not in s:
            return
        s.discard((x,y))
        for dx, dy in near(x, y):
            start_from_seed(dx, dy)
    out = []

    while len(s) != 0:
        start_from_seed(*tuple(s)[0])
        diff = k - s
        k = s.copy()
        out.append((len(diff), diff))
    return out


def find_all_small_regions(s):
    out = []
    pops = set(i[0] for i in s)
    if len(pops) == 1:
        return out
    minn = min(pops)
    for i in s:
        if i[0] == minn:
            out.extend(i[1])
    return out


def find_all_not_biggest_regions(s):
    out = []
    pops = set(i[0] for i in s)
    if len(pops) == 1:
        return out
    minn = max(pops)
    for i in s:
        if i[0] < minn:
            out.extend(i[1])
    return out



def find_groups_Neumann2(k):

    s = k.copy()

    def near2(x,y):
        return ((x,y+1),(x+1,y),(x-1,y),(x,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1),(x,y+2),(x+2,y),(x-2,y),(x,y-2))

    def start_from_seed(x,y):
        if (x,y) not in s:
            return
        s.discard((x,y))
        for dx, dy in near2(x, y):
            start_from_seed(dx, dy)
    out = []

    while len(s) != 0:
        start_from_seed(*tuple(s)[0])
        diff = k - s
        k = s.copy()
        out.append( diff )
    return out

# def not_biggest_connected_in_groups(inp):
#     groups = find_groups_Neumann2(inp)
#     out = []
#     for i in groups:
#         out.extend(find_all_not_biggest_regions(i))

#     return out


