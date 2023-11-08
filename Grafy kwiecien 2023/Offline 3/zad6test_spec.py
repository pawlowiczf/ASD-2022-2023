# zad6test_spec.py
from math import sqrt

ALLOWED_TIME = 1000


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  # n e/M  hint
  # n - number of workers
  # e/M - number of edges per worker +/- sqrt(e), or the explicit matrix (if n = 0)
  # hint - value of the solution
  (0, [ [ 0, 1, 3],
        [ 2, 4],
        [ 0, 2],
        [ 3 ],
        [ 3, 2] ], 5
  ),
  (0, [[0,1], [0,1], [0]], 2 ),
  (10, 4, 10),
  (20, 4, 19),
  (50, 10, 50),
  (500, 10, 500),
  (1500, 4, 1468),
  (500, 2, 410),
  (500, 50, 500),
  (1000, 3, 942),
]


from testy import MY_random

def my_randint(a,b):
  return a+MY_random()%(b-a+1)

def gentest(test, arg, hint ):
  n = test
  if test==0:
    return [arg],hint
  
  e = arg
  M = [ [] for i in range(n) ]
  for i in range(n):
    num = my_randint( e - int(sqrt(e)), e + int(sqrt(e)) )
    mach = set()
    for j in range( num ):
      mach.add( my_randint( 0, n-1 ) )
    M[i] = list( mach ) 

  return [M],hint
   

  
