# zad6test_spec.py

ALLOWED_TIME = 1000

from random import randint,shuffle
end = None

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
  ( 0,  [(10,10),(15,25),(20,20),(30,40)],7 ),
  ( 0,  [(23,56),(12,120),(45,98),(73,37),(1,101)], 14 ),
  ( 0,  [(100,100),(100,200),(200,100),(200,200)], 0 ),
  ( 0,  [(100,100),(100,200),(210,100),(210,200)], 10 ),
  ( 0,  [(100,100),(100,200),(200,100),(200,200),(150,151)], 1 ),
  ( 10, [], 62 ),
  ( 20, [], 73 ),
  ( 30, [], 61 ),
  ( 50, [], 38 ),
  ( 100, [], 25 ),
 ]


def gentest(n,arg,hint):
    from testy import MY_random

    if n==0:
      return [arg], hint
    else:
      arg = [(MY_random()%1000,MY_random()%1000) for _ in range(n)]
      return [arg], hint

    exit()
