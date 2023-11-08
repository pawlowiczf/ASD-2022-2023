# zad6test_spec.py

ALLOWED_TIME = 1000

from random import randint,shuffle
end = None

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  ( 0, [(0,1,10),(1,2,2),(1,3,5),(1,4,3)], 0, 10 ),
  ( 1, [(0,1,15),(1,2,2),(1,3,15),(1,4,3),(0,2,7),(0,4,6)], 0, 22 ),
  ( 2, [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),(3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)], 2, 25),
  ( 3, [(0,1,12),(0,2,10),(0,3,12),(1,4,8),(2,4,2),(2,5,2),(3,5,8),(4,6,10),(4,7,2),(5,7,2),(5,8,10)], 0, 24),
  ( 4, [(0,1,12),(0,2,10),(0,3,12),(1,4,8),(2,4,2),(2,5,2),(3,5,8),(4,6,10),(4,7,2),(5,7,2),(5,8,10),(1,6,5)], 0, 26),
  ( 5, [], 0, 159 ),
  ( 6, [], 0, 144 ),
 ]


def gentest(n,G,s,hint):
    from testy import MY_random

    if n<5:
      return  [G,s], hint
    else:
      N=2**n
      G = []
      for i in range(N//2):
        G.append((i,2*i+1,MY_random()%100))
        G.append((i,2*i+2,MY_random()%100))
      for i in range(N//2):
        x = N//2+MY_random()%(N//2)
        if x>2*i+1:
          G.append((i,x,MY_random()%100))

      return [G,0], hint

    exit()
