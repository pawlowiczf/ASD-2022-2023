# egz3atest_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100

from testy import MY_random
from math  import inf

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# n, p, e
# n - liczba zamkow
# p - liczba gwarantowanych sciezek z s=0 do t=n-1
# e - liczba dodatkowych losowych krawedzi
TEST_SPEC = [
  (10,2, 6, 12),
  (20,3, 20, 26),
  (40,2, 10, 40),
  (100,5, 30, 37),
  (200,1, 400, 27),
  (500,2, 200, 14),
  (500,1, 100, 54),
]


def genpath( G ):
    n = len(G)
    act = 0

    while True:
        nxt = act + 1 + (MY_random()%8)
        if nxt >= n: break
        wgt = 1+(MY_random()%8)
        G[act][nxt] = wgt
        G[nxt][act] = wgt
        act = nxt

    if G[act][n-1] == -1:
        wgt = 1+(MY_random()%8)
        G[act][n-1] = wgt
        G[n-1][act] = wgt


def gentest(n, p, e, hint):
    print(f"###################### {n-1}")

    G = [[-1 for _ in range(n)] for __ in range(n)]

    # dodaj losowe krawedzie
    for i in range(e):
        u = MY_random() % n
        v = 1+MY_random() % 30
        if v >= n: continue
        wgt = 1+(MY_random()%8)
        G[u][v] = wgt
        G[v][u] = wgt

    # dodaj gwarantowane sciezki
    for i in range(p):
        genpath( G )

    return [G,0,n-1], hint
