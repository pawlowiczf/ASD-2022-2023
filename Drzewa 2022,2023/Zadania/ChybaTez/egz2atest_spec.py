# egz1atest_spec.py

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n  T hint
  (10, 10, 6),
  (20, 30, 10),
  (800, 30, 58),
  (2000, 30, 996),
  (10000, 5000, 5147),
  (10000, 1, 9999),
  (20000, 100, 10290),
  (30000, 10, 16562),
  (30000, 10000, 15236),
  ]


from testy import MY_random

def my_randint(a,b):
    return a+MY_random()%(b-a+1)

def gentest(n, T, hint):
    A = [my_randint(1, T) for _ in range(n)]
    return [A,T], hint

