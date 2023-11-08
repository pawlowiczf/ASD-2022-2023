# egz2btest_spec.py
from testy import *
import sys
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  (10,20, 10, 6 ,48),
  (50,200, 20, 5 ,44),
  (100,300, 30, 10 ,221),
  (200,300, 30, 20 ,1092),
  (200,600, 60, 20 ,789),
  (400,600, 6, 4 ,352),
  (300,1000, 6, 2 ,84),
  (500,1000, 10, 5 ,552),
  (10,10000, 1000, 5 ,17),
  (300,3000, 10, 1 ,6),
]


def genlist( n, step ):
    L = [0]*n
    L[0] = MY_random()%30
    for i in range(1,n):
        L[i] = (L[i-1]+MY_random()%step)+1
    return L


def gentest(n,m, step_n, step_m, hint):
    from testy import MY_random


    X = genlist( n, step_n )
    Y = genlist( m, step_m )

    return [X,Y], hint
