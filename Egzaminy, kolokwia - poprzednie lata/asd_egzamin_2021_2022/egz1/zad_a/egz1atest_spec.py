# egz1atest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n  s hint
  (500, 50, 1223),
  (1000, 500, 82321),
  (1500, 500, 93557),
  (2000, 1000, 340812),
  (20000, 1000, 478277),
  (20000, 2000, 1822062),
  (200000, 10000, 47633556),
  (500000, 10000, 49039734),
  (1000000, 10000, 49531270),
]


from testy import MY_random

def my_randint(a,b):
    return a+MY_random()%(b-a+1)

def gentest(n, s, hint):
    S = [my_randint(1, s+1) for _ in range(n)]
    return [S], hint

