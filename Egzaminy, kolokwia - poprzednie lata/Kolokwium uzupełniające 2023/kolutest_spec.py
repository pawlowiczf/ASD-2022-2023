# kolutest_spec.py

import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  (10, 20, 80),
  (10000, 15000, 44805174),
  (10000, 30000, 112810793),
  (20000, 80000, 642954449),
  (30000, 100000, 1149827513),
  (50000, 500000, 11375538451),
  (100000, 10000000, 493342158357),
  (500000, 50000000, 12368312124029),
  (1000000, 100000000, 49424994484589),
]


def gentest(n, m, hint):
    from testy import MY_random

    T = [MY_random() % m for _ in range(n)]

    return [T], hint
