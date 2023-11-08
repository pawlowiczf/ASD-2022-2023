# egz2atest_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  (10,6),
  (100,85),
  (500,477),
  (3000,2991),
  (10000,9892),
  (20000,19775),
  (100000,99740),
  (300000,299713),
  (600000,598717),
  (1200000,1198561),
]


def gentest(n, hint):
    from testy import MY_random

    DATA = set()

    P = [(0,0)]*n
    last = 0
    for i in range(n):
        while True:
          x = MY_random()%n + 1
          y = MY_random()%n + 1
          if (x,y) not in DATA:
            DATA.add((x,y))          
            P[i] = (x,y)
            break

    return [P], hint
