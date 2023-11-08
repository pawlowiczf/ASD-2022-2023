# egz3btest_spec.py
import sys
from random import *
seed(0)
sys. setrecursionlimit(1000000)

ALLOWED_TIME = 100

from testy import MY_random
from math  import inf

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

# n, k, hint
# n - rozmiar tablicy
# k - parametr k
TEST_SPEC = [
  (0,1000,10, 3, -1),
  (0,1000,100, 3, -1),
  (0,10000,100, 5, -1),
  (0,10000,300, 4, -1),
  (0,100000,1000, 7, -1),
  (0,200000,2000, 7, -1),
  (0,300000,5000, 10, -1),
  (0,300000,7000, 10, -1),
  (0,300000,10000, 10, -1),
  (0,300000,15000, 10, -1),
]


def genlam( a, b, d ):
    if d == 0: return []
#    print( f"d = {d}")

    R = []
    x = a + MY_random() % 5

    while x <= b:
       l = b-x+1
       y = x + 1 + (MY_random() % l)
       if y > b: break
       R += [[x,y]]
#       print( f"{[x,y]}")
       R += genlam( x,y,d-1 )
       x = y + 2 + MY_random() % 5

    return R
       
        



def gentest(a,b,n, d, hint):
    P = genlam( a,b,d )
    P = P[0:n]
    n = len(P)
    shuffle( P )
    i = MY_random() % (n//2)
    j = n//2 + MY_random() % (n//2)
    A = P[0:i]
    B = P[i:j]
    C = P[j:n]

    x0 = a + MY_random() % (b-a)
    x1 = x0 + 1 + MY_random() % (b-a)
    x2 = x1 + 1 + MY_random() % (b-a)
    x3 = x2 + 1 + MY_random() % (b-a)

    P = A + [[x0,x2]] + B +  [[x1,x3]] + C

    hint = f"{(i,j+1)} ==> {P[i]}, {P[j+1]}"

    return [P], hint
