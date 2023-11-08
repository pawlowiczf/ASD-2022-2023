# egz1btest_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  (11, 5, 10, 20),
  (101, 5, 10, 146),
  (101, 10, 10, 235),
  (1001, 10, 100, 17729),
  (1001, 10, 100, 16591),
  (5001, 10, 100, 72940),
  (5001, 15, 100, 93752),
  (10001, 15, 100, 197307),
  (10001, 20, 100, 231036),
]


def gentest(n, t, mp, hint):
    from testy import MY_random

    D, C, T = [-1]*n, [-1]*n, [(0,0)]*n
    last = 0
    for i in range(n):
        D[i] = last
        C[i] = MY_random() % mp + 1
        last = D[i] + MY_random() % ((2*t)//3) + 1
        j = (MY_random() % 20)-5
        if j < 0: j = 0
        p = MY_random() % ((2*C[i]*j//3) + 2)
        j = i+j
        if j >= n-1: j = n-1
        T[i] = (j,p)
    B = t

    return [D, C, T, B], hint
